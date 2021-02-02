import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from globar_var import DRIVER_PATH

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def get_news(url, focused_href, focused_class) :
    driver.get(url)
    links = driver.find_elements_by_tag_name("a")
    links = list(dict.fromkeys(links))
    opened_tab = []
    texts = []
    for link in links:
        if (focused_href in elem.get_attribute("href")) and (link.get_attribute("href") not in opened_tab) :
            y = elem.location["y"]
            java_script = f"window.scrollBy(0,{y});"
            driver.execute_script(java_script)
            main_window = driver.current_window_handle
            elem.send_keys(Keys.CONTROL + Keys.RETURN)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            paragraphs = driver.find_elements_by_xpath(focused_class)
            for p in paragraphs :
                texts.append(p.text)
            driver.close()
            driver.switch_to_window(main_window)
            opened_tab.append(link.get_attribute("href"))
    return texts

driver.get("https://money.kompas.com/whatsnew")
elems = driver.find_elements_by_tag_name("a")
elems = list(dict.fromkeys(elems))
opened_tab = []
texts = []
for elem in elems:
    if ("https://money.kompas.com/read" in elem.get_attribute("href")) and (elem.get_attribute("href") not in opened_tab) :
        y = elem.location["y"]
        javaScript = f"window.scrollBy(0,{y});"
        driver.execute_script(javaScript)
        main_window = driver.current_window_handle
        elem.send_keys(Keys.CONTROL + Keys.RETURN)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        paragraphs = driver.find_elements_by_xpath("//div[@class='read__content']/div/p")
        for p in paragraphs :
            texts.append(p.text)
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        driver.close()
        driver.switch_to_window(main_window)
        opened_tab.append(elem.get_attribute("href"))
print(texts)
driver.quit()