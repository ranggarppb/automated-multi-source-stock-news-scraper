import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from globar_var import DRIVER_PATH, LIST_STOCKS, KOMPAS_CONFIG, CNN_CONFIG, DETIK_CONFIG, TEMPO_CONFIG, CNBC_CONFIG, LIPUTAN6_CONFIG

def get_news_certain_stock(url, focused_search_xpath, stock, focused_submit_xpath, focused_link_xpath, focused_link_href, focused_text_class) :
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(url)
    try : 
        driver.find_element_by_xpath(focused_search_xpath).send_keys(stock)
        driver.find_element_by_xpath(focused_submit_xpath).click()
    except :
        driver.find_element_by_xpath(focused_submit_xpath).click()
        driver.find_element_by_xpath(focused_search_xpath).send_keys(stock)
        driver.find_element_by_xpath(focused_search_xpath).send_keys(Keys.ENTER)
    links = driver.find_elements_by_xpath(focused_link_xpath)
    links = list(dict.fromkeys(links))
    opened_tab = []
    texts = []
    for link in links:
        try : 
            if (focused_link_href in link.get_attribute("href")) and (link.get_attribute("href") not in opened_tab) :
                    y = link.location["y"]
                    java_script = f"window.scrollBy(0,{y});"
                    driver.execute_script(java_script)
                    main_window = driver.current_window_handle
                    link.send_keys(Keys.CONTROL + Keys.RETURN)
                    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                    windows = driver.window_handles
                    driver.switch_to_window(windows[1])
                    paragraphs = driver.find_elements_by_xpath(focused_text_class)
                    for p in paragraphs :
                        texts.append(p.text)
                    driver.close()
                    driver.switch_to_window(main_window)
                    opened_tab.append(link.get_attribute("href"))
        except :
            pass
    driver.close()
    return texts

def get_news_overall(url, focused_link_xpath, focused_link_href, focused_text_class) :
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(url)
    links = driver.find_elements_by_xpath(focused_link_xpath)
    links = list(dict.fromkeys(links))
    opened_tab = []
    texts = []
    for link in links:
        try : 
            if (focused_link_href in link.get_attribute("href")) and (link.get_attribute("href") not in opened_tab) :
                    y = link.location["y"]
                    java_script = f"window.scrollBy(0,{y});"
                    driver.execute_script(java_script)
                    main_window = driver.current_window_handle
                    link.send_keys(Keys.CONTROL + Keys.RETURN)
                    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                    windows = driver.window_handles
                    driver.switch_to_window(windows[1])
                    paragraphs = driver.find_elements_by_xpath(focused_text_class)
                    for p in paragraphs :
                        texts.append(p.text)
                    driver.close()
                    driver.switch_to_window(main_window)
                    opened_tab.append(link.get_attribute("href"))
        except :
            pass
    driver.close()
    return texts

def main():

    news = {}

    kompas_per_stock = {}
    for stock in LIST_STOCKS :
        kompas_news_certain_stock = get_news_certain_stock(KOMPAS_CONFIG["URL"], KOMPAS_CONFIG["SEARCH_XPATH"], stock, KOMPAS_CONFIG["SUBMIT_XPATH"], 
        KOMPAS_CONFIG["LINK_XPATH"], KOMPAS_CONFIG["LINK_HREF"], KOMPAS_CONFIG["TEXT_CLASS"])
        kompas_per_stock.update({stock:kompas_news_certain_stock})
    kompas_news_overall = get_news_overall(KOMPAS_CONFIG["URL"], KOMPAS_CONFIG["LINK_XPATH"], KOMPAS_CONFIG["LINK_HREF"], KOMPAS_CONFIG["TEXT_CLASS"])
    news.update({"kompas":{"kompas_certain_stock":kompas_per_stock, "kompas_overall":kompas_news_overall}})

    cnn_per_stock = {}
    for stock in LIST_STOCKS :
        cnn_news_certain_stock = get_news_certain_stock(CNN_CONFIG["URL"], CNN_CONFIG["SEARCH_XPATH"], stock, CNN_CONFIG["SUBMIT_XPATH"], 
        CNN_CONFIG["LINK_XPATH"], CNN_CONFIG["LINK_HREF"], CNN_CONFIG["TEXT_CLASS"])
        cnn_per_stock.update({stock:cnn_news_certain_stock})
    cnn_news_overall = get_news_overall(CNN_CONFIG["URL"], CNN_CONFIG["LINK_XPATH"],  CNN_CONFIG["LINK_HREF"], CNN_CONFIG["TEXT_CLASS"])
    news.update({"cnn":{"cnn_certain_stock":cnn_per_stock, "cnn_overall":cnn_news_overall}})

    detik_per_stock = {}
    for stock in LIST_STOCKS :
        detik_news_certain_stock = get_news_certain_stock(DETIK_CONFIG["URL"], DETIK_CONFIG["SEARCH_XPATH"], stock, DETIK_CONFIG["SUBMIT_XPATH"], 
        DETIK_CONFIG["LINK_XPATH"], DETIK_CONFIG["LINK_HREF"], DETIK_CONFIG["TEXT_CLASS"])
        detik_per_stock.update({stock:detik_news_certain_stock})
    detik_news_overall = get_news_overall(DETIK_CONFIG["URL"], DETIK_CONFIG["LINK_XPATH"],  DETIK_CONFIG["LINK_HREF"], DETIK_CONFIG["TEXT_CLASS"])
    news.update({"detik":{"detik_certain_stock":detik_per_stock, "detik_overall":detik_news_overall}})

    tempo_per_stock = {}
    for stock in LIST_STOCKS :
        tempo_news_certain_stock = get_news_certain_stock(TEMPO_CONFIG["URL"], TEMPO_CONFIG["SEARCH_XPATH"], stock, TEMPO_CONFIG["SUBMIT_XPATH"], 
        TEMPO_CONFIG["LINK_XPATH"], TEMPO_CONFIG["LINK_HREF"], TEMPO_CONFIG["TEXT_CLASS"])
        tempo_per_stock.update({stock:tempo_news_certain_stock})
    tempo_news_overall = get_news_overall(TEMPO_CONFIG["URL"], TEMPO_CONFIG["LINK_XPATH"],  TEMPO_CONFIG["LINK_HREF"], TEMPO_CONFIG["TEXT_CLASS"])
    news.update({"tempo":{"tempo_certain_stock":tempo_per_stock, "tempo_overall":tempo_news_overall}})

    cnbc_per_stock = {}
    for stock in LIST_STOCKS :
        cnbc_news_certain_stock = get_news_certain_stock(CNBC_CONFIG["URL"], CNBC_CONFIG["SEARCH_XPATH"], stock, CNBC_CONFIG["SUBMIT_XPATH"], 
        CNBC_CONFIG["LINK_XPATH"], CNBC_CONFIG["LINK_HREF"], CNBC_CONFIG["TEXT_CLASS"])
        cnbc_per_stock.update({stock:cnbc_news_certain_stock})
    cnbc_news_overall = get_news_overall(CNBC_CONFIG["URL"], CNBC_CONFIG["LINK_XPATH"],  CNBC_CONFIG["LINK_HREF"], CNBC_CONFIG["TEXT_CLASS"])
    news.update({"cnbc":{"cnbc_certain_stock":cnbc_per_stock, "cnbc_overall":cnbc_news_overall}})

    liputan6_per_stock = {}
    for stock in LIST_STOCKS :
        liputan6_news_certain_stock = get_news_certain_stock(LIPUTAN6_CONFIG["URL"], LIPUTAN6_CONFIG["SEARCH_XPATH"], stock, LIPUTAN6_CONFIG["SUBMIT_XPATH"], 
        LIPUTAN6_CONFIG["LINK_XPATH"], LIPUTAN6_CONFIG["LINK_HREF"], LIPUTAN6_CONFIG["TEXT_CLASS"])
        liputan6_per_stock.update({stock:liputan6_news_certain_stock})
    liputan6_news_overall = get_news_overall(LIPUTAN6_CONFIG["URL"], LIPUTAN6_CONFIG["LINK_XPATH"],  LIPUTAN6_CONFIG["LINK_HREF"], LIPUTAN6_CONFIG["TEXT_CLASS"])
    news.update({"liputan6":{"liputan6_certain_stock":liputan6_per_stock, "liputan6_overall":liputan6_news_overall}})

if __name__ == '__main__':
    main()
