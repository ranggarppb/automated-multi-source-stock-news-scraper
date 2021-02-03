"""

Collection of configuration variables

"""
from utils import config_reader
CONFIG_FILE="config.ini"

config_news_scraper = config_reader(CONFIG_FILE, section="news_scraper")
kompas_config = config_reader(CONFIG_FILE, section="kompas_config")
cnn_config = config_reader(CONFIG_FILE, section="cnn_config")
detik_config = config_reader(CONFIG_FILE, section="detik_config")
tempo_config = config_reader(CONFIG_FILE, section="tempo_config")
cnbc_config = config_reader(CONFIG_FILE, section="cnbc_config")
liputan6_config = config_reader(CONFIG_FILE, section="liputan6_config")

# configuration of news scraper
DRIVER_PATH = config_news_scraper["driver_path"]
LIST_STOCKS = config_news_scraper["list_stocks"].split(",")

# configuration of money kompas site
KOMPAS_URL = kompas_config["url"]
KOMPAS_SEARCH_XPATH = kompas_config["focused_search_xpath"]
KOMPAS_SUBMIT_XPATH = kompas_config["focused_submit_xpath"]
KOMPAS_LINK_XPATH = kompas_config["focused_link_xpath"]
KOMPAS_LINK_HREF = kompas_config["focused_link_href"]
KOMPAS_TEXT_CLASS = kompas_config["focused_text_class"]
KOMPAS_CONFIG = {
    "URL":KOMPAS_URL,
    "SEARCH_XPATH":KOMPAS_SEARCH_XPATH,
    "SUBMIT_XPATH":KOMPAS_SUBMIT_XPATH,
    "LINK_XPATH":KOMPAS_LINK_XPATH,
    "LINK_HREF":KOMPAS_LINK_HREF,
    "TEXT_CLASS":KOMPAS_TEXT_CLASS
    }

# configuration of cnn ekonomi site
CNN_URL = cnn_config["url"]
CNN_SEARCH_XPATH = cnn_config["focused_search_xpath"]
CNN_SUBMIT_XPATH = cnn_config["focused_submit_xpath"]
CNN_LINK_XPATH = cnn_config["focused_link_xpath"]
CNN_LINK_HREF = cnn_config["focused_link_href"]
CNN_TEXT_CLASS = cnn_config["focused_text_class"]

CNN_CONFIG = {
    "URL":CNN_URL,
    "SEARCH_XPATH":CNN_SEARCH_XPATH,
    "SUBMIT_XPATH":CNN_SUBMIT_XPATH,
    "LINK_XPATH":CNN_LINK_XPATH,
    "LINK_HREF":CNN_LINK_HREF,
    "TEXT_CLASS":CNN_TEXT_CLASS
    }

# configuration of DETIK ekonomi site
DETIK_URL = detik_config["url"]
DETIK_SEARCH_XPATH = detik_config["focused_search_xpath"]
DETIK_SUBMIT_XPATH = detik_config["focused_submit_xpath"]
DETIK_LINK_XPATH = detik_config["focused_link_xpath"]
DETIK_LINK_HREF = detik_config["focused_link_href"]
DETIK_TEXT_CLASS = detik_config["focused_text_class"]

DETIK_CONFIG = {
    "URL":DETIK_URL,
    "SEARCH_XPATH":DETIK_SEARCH_XPATH,
    "SUBMIT_XPATH":DETIK_SUBMIT_XPATH,
    "LINK_XPATH":DETIK_LINK_XPATH,
    "LINK_HREF":DETIK_LINK_HREF,
    "TEXT_CLASS":DETIK_TEXT_CLASS
    }

# configuration of tempo bisnis site
TEMPO_URL = tempo_config["url"]
TEMPO_SEARCH_XPATH = tempo_config["focused_search_xpath"]
TEMPO_SUBMIT_XPATH = tempo_config["focused_submit_xpath"]
TEMPO_LINK_XPATH = tempo_config["focused_link_xpath"]
TEMPO_LINK_HREF = tempo_config["focused_link_href"]
TEMPO_TEXT_CLASS = tempo_config["focused_text_class"]

TEMPO_CONFIG = {
    "URL":TEMPO_URL,
    "SEARCH_XPATH":TEMPO_SEARCH_XPATH,
    "SUBMIT_XPATH":TEMPO_SUBMIT_XPATH,
    "LINK_XPATH":TEMPO_LINK_XPATH,
    "LINK_HREF":TEMPO_LINK_HREF,
    "TEXT_CLASS":TEMPO_TEXT_CLASS
    }

# configuration of CNBC bisnis site
CNBC_URL = cnbc_config["url"]
CNBC_SEARCH_XPATH = cnbc_config["focused_search_xpath"]
CNBC_SUBMIT_XPATH = cnbc_config["focused_submit_xpath"]
CNBC_LINK_XPATH = cnbc_config["focused_link_xpath"]
CNBC_LINK_HREF = cnbc_config["focused_link_href"]
CNBC_TEXT_CLASS = cnbc_config["focused_text_class"]

CNBC_CONFIG = {
    "URL":CNBC_URL,
    "SEARCH_XPATH":CNBC_SEARCH_XPATH,
    "SUBMIT_XPATH":CNBC_SUBMIT_XPATH,
    "LINK_XPATH":CNBC_LINK_XPATH,
    "LINK_HREF":CNBC_LINK_HREF,
    "TEXT_CLASS":CNBC_TEXT_CLASS
    }

# configuration of LIPUTAN6 bisnis site
LIPUTAN6_URL = liputan6_config["url"]
LIPUTAN6_SEARCH_XPATH = liputan6_config["focused_search_xpath"]
LIPUTAN6_SUBMIT_XPATH = liputan6_config["focused_submit_xpath"]
LIPUTAN6_LINK_XPATH = liputan6_config["focused_link_xpath"]
LIPUTAN6_LINK_HREF = liputan6_config["focused_link_href"]
LIPUTAN6_TEXT_CLASS = liputan6_config["focused_text_class"]

LIPUTAN6_CONFIG = {
    "URL":LIPUTAN6_URL,
    "SEARCH_XPATH":LIPUTAN6_SEARCH_XPATH,
    "SUBMIT_XPATH":LIPUTAN6_SUBMIT_XPATH,
    "LINK_XPATH":LIPUTAN6_LINK_XPATH,
    "LINK_HREF":LIPUTAN6_LINK_HREF,
    "TEXT_CLASS":LIPUTAN6_TEXT_CLASS
    }