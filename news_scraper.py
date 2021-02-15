import re
import pickle
import collections
import os
import sys
import jsonlines
from datetime import datetime
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, StaleElementReferenceException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from google.cloud import storage
from utils import list_duplicates
import global_var
from global_var import DRIVER_PATH, GOOGLE_STORAGE_CONFIG, LIST_STOCKS, NEWS_SOURCES, SOURCES_TO_CONFIG_MAPPINGS, NUMBER_OF_NEWS, NEWS_DB_TMP

def get_listed_links(news_db_today, focused_item) :
    if len(news_db_today) != 0 :
        links_per_scheduled_hours = [list(news.items())[0][1] for news in news_db_today]
        links_per_source_today_dict = [x[focused_item][source] for x in links_per_scheduled_hours]
        links_per_source_today = []
        for links_dict in links_per_source_today_dict :
            links_per_source_today += list(links_dict.keys())
    else :
        links_per_source_today = []

    return links_per_source_today

def map_source_to_config(source) :

    config = getattr(global_var, SOURCES_TO_CONFIG_MAPPINGS[source])

    return config

def search_in_searchbar(driver, search_bar_icon, search_bar_input, keyword) :
    
    wait = WebDriverWait(driver,45)
    # clink the search bar icon
    wait.until(EC.element_to_be_clickable((By.XPATH,search_bar_icon))).click()
    # type the search keyword
    wait.until(EC.presence_of_element_located((By.XPATH,search_bar_input))).send_keys(keyword)
    try : 
        # press enter to begin search
        driver.find_element_by_xpath(search_bar_input).send_keys(Keys.ENTER)
    except NoSuchElementException :
        # send enter to search icon
        driver.find_element_by_xpath(search_bar_icon).send_keys(Keys.ENTER)

    return driver

def get_necessary_links_and_its_positions(number_of_news, focused_news_segment, links_per_source_today, anchors, links, y_positions) :
    
    # throw away none, get the index of none, and delete y_positions based on the index
    ind_none = [i for i, v in enumerate(links) if v is None]
    links = [links[i] for i in range(len(links)) if i not in ind_none]
    y_positions = [y_positions[i] for i in range(len(y_positions)) if i not in ind_none]
    anchors = [anchors[i] for i in range(len(anchors)) if i not in ind_none]

    # throw away duplicated links, get the index of duplicated links, and delete y_positions based on the index
    ind_duplicates = list_duplicates(links)  
    ind_duplicates_all = []
    for element in ind_duplicates :
        ind_duplicate_per_element = element[1][1:]
        ind_duplicates_all += ind_duplicate_per_element  

    links = [links[i] for i in range(len(links)) if i not in ind_duplicates_all]
    y_positions = [y_positions[i] for i in range(len(y_positions)) if i not in ind_duplicates_all]
    anchors = [anchors[i] for i in range(len(anchors)) if i not in ind_duplicates_all]

    # throw away unimportant news get the index of unimportant news, and delete y_positions based on the index
    ind_selected_news = [i for i, v in enumerate(links) if re.match(focused_news_segment, v)]
    links = [links[i] for i in range(len(links)) if i in ind_selected_news]
    y_positions = [y_positions[i] for i in range(len(y_positions)) if i in ind_selected_news]
    anchors = [anchors[i] for i in range(len(anchors)) if i in ind_selected_news]

    # throw away any already scrapped links
    ind_scrapped_links = [i for i, v in enumerate(links) if v in links_per_source_today]
    links = [links[i] for i in range(len(links)) if i not in ind_scrapped_links]
    y_positions = [y_positions[i] for i in range(len(y_positions)) if i not in ind_scrapped_links]
    anchors = [anchors[i] for i in range(len(anchors)) if i not in ind_scrapped_links]

    # get only latest news
    links = links[:number_of_news]
    y_positions = y_positions[:number_of_news]
    anchors = anchors[:number_of_news]

    return anchors, links, y_positions

def open_links_and_get_news(driver, anchors, links, y_positions, text_class, date_class) :

    wait = WebDriverWait(driver,45)
    main_window = driver.current_window_handle
    news_dictionary = {}
    if len(links) != 0 : 
        last_non_zero_position = y_positions[0]
        for i in range(len(links)) : 
            try : 
                scroll_to_y = f"window.scrollBy(0,{last_non_zero_position});"
                driver.execute_script(scroll_to_y)
                anchors[i].send_keys(Keys.CONTROL + Keys.RETURN)
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                sleep(10)
                wait.until(EC.presence_of_element_located((By.XPATH,text_class)))
                paragraphs = driver.find_elements_by_xpath(text_class)
                texts = [p.text for p in paragraphs if p.text != '']
                texts = " ".join(texts)
                wait.until(EC.presence_of_element_located((By.XPATH,date_class)))
                date = driver.find_element_by_xpath(date_class)
                date = date.text 
                news_dictionary.update({links[i]:{"date":date, "news":texts}})
                driver.close()
                driver.switch_to_window(main_window) 
                scroll_to_initial = f"window.scrollBy(0,{-last_non_zero_position});"
                driver.execute_script(scroll_to_initial)
                if y_positions[i] > 0 : 
                    last_non_zero_position = y_positions[i]
            except (TimeoutException, StaleElementReferenceException, ElementNotInteractableException) :
                pass

    return news_dictionary

def search_from_certain_source(driver_options, config, links_per_source_today, stock=None, mode="overall") :

    driver = webdriver.Chrome(options=driver_options, executable_path=DRIVER_PATH)
    wait = WebDriverWait(driver, 45)
    driver.set_page_load_timeout(60)
     # open the config
    main_page_url = config["URL"]
    search_bar = config["SEARCH_BAR"]
    search_bar_icon = config["SEARCH_ICON"]
    anchor_tag = config["ANCHOR_TAG"]
    focused_news_segment = config["LINK_HREF"]
    text_class = config["TEXT_CLASS"]
    date_class = config["DATE_CLASS"]  
    number_of_news = NUMBER_OF_NEWS
    try : 
        # go to main page
        driver.get(main_page_url)
        sleep(10)
        if mode == "per_stock" : 
            # search certain stock keyword in search bar
            driver = search_in_searchbar(driver, search_bar_icon, search_bar, stock)
        # get all news links in the page and their positions in the page so we can open them later
        wait.until(EC.presence_of_element_located((By.XPATH, anchor_tag)))
        anchors = driver.find_elements_by_xpath(anchor_tag)
        links = [anchor.get_attribute("href") for anchor in anchors]
        y_positions = [anchor.location["y"] for anchor in anchors]
        # filter only necessary links (and so only necessary positions)
        sleep(10)
        anchors, links, y_positions = get_necessary_links_and_its_positions(number_of_news, focused_news_segment, links_per_source_today, anchors, links, y_positions)
        # get news from links
        news_per_source = open_links_and_get_news(driver, anchors, links, y_positions, text_class, date_class)
    except (TimeoutException, WebDriverException) :
        news_per_source = {}

    return news_per_source

if __name__ == '__main__':

    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')

    storage_client = storage.Client.from_service_account_json(GOOGLE_STORAGE_CONFIG["SERVICE_ACCOUT_CREDENTIAL"])
    bucket = storage_client.get_bucket(GOOGLE_STORAGE_CONFIG["STORAGE_BUCKET"])
    blob = bucket.get_blob(GOOGLE_STORAGE_CONFIG["DATA_FILE"])
    blob.download_to_filename(NEWS_DB_TMP)

    current_datetime = datetime.today().strftime('%Y-%m-%d %H')

    with jsonlines.open(NEWS_DB_TMP) as database_input:
        news_db = list(database_input)

    news_data = {}
    news_sources = NEWS_SOURCES

    for stock in LIST_STOCKS : 
        news_per_stock = {}
        for source in news_sources :
            config = map_source_to_config(source)
            links_per_source_today = get_listed_links(news_db, stock)
            news_per_source = search_from_certain_source(options, config, links_per_source_today, stock=stock, mode="per_stock")
            news_per_stock.update({source:news_per_source})
        news_data.update({stock:news_per_stock})
    
    news_overall = {}
    for source in news_sources :
        config = map_source_to_config(source)
        links_per_source_today = get_listed_links(news_db, "OVERALL")
        news_overall_per_source = search_from_certain_source(options, config, links_per_source_today, mode="overall")
        news_overall.update({source:news_overall_per_source})
    news_data.update({"OVERALL":news_overall})

    with jsonlines.open(NEWS_DB_TMP, mode='a') as database_output:
        database_output.write({current_datetime:news_data})
    blob.upload_from_filename(NEWS_DB_TMP)