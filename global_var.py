"""

Collection of configuration variables

"""
from utils import config_reader
import json
CONFIG_FILE="config.ini"

config_google_storage = config_reader(CONFIG_FILE, section="google_storage")
config_news_scraper = config_reader(CONFIG_FILE, section="news_scraper")
kompas_config = config_reader(CONFIG_FILE, section="kompas_config")
cnn_config = config_reader(CONFIG_FILE, section="cnn_config")
detik_config = config_reader(CONFIG_FILE, section="detik_config")
tempo_config = config_reader(CONFIG_FILE, section="tempo_config")
cnbc_config = config_reader(CONFIG_FILE, section="cnbc_config")
liputan6_config = config_reader(CONFIG_FILE, section="liputan6_config")

# configuration of google cloud storage to read and store raw news data
SERVICE_ACCOUNT_CREDENTIAL = config_google_storage["service_account_credential"]
STORAGE_BUCKET = config_google_storage["storage_bucket"]
DATA_FILE = config_google_storage["data_file"]
GOOGLE_STORAGE_CONFIG = {
    "SERVICE_ACCOUNT_CREDENTIAL":SERVICE_ACCOUNT_CREDENTIAL,
    "STORAGE_BUCKET":STORAGE_BUCKET,
    "DATA_FILE":DATA_FILE
}

# configuration of news scraper
DRIVER_PATH = config_news_scraper["driver_path"]
LIST_STOCKS = config_news_scraper["list_stocks"].split(",")
NEWS_SOURCES = config_news_scraper["news_sources"].split(",")
SOURCES_TO_CONFIG_MAPPINGS = json.loads(config_news_scraper["sources_to_config_mappings"])
NUMBER_OF_NEWS = int(config_news_scraper["number_of_news"])
NEWS_DB_TMP = config_news_scraper["news_db_tmp"]

# configuration of money kompas site
KOMPAS_URL = kompas_config["url"]
KOMPAS_SEARCH_BAR = kompas_config["search_bar"]
KOMPAS_SEARCH_ICON = kompas_config["search_icon"]
KOMPAS_ANCHOR_TAG = kompas_config["anchor_tag"]
KOMPAS_LINK_HREF = kompas_config["link_href"]
KOMPAS_TEXT_CLASS = kompas_config["text_class"]
KOMPAS_DATE_CLASS =  kompas_config["date_class"]
KOMPAS_CONFIG = {
    "URL":KOMPAS_URL,
    "SEARCH_BAR":KOMPAS_SEARCH_BAR,
    "SEARCH_ICON":KOMPAS_SEARCH_ICON,
    "ANCHOR_TAG":KOMPAS_ANCHOR_TAG,
    "LINK_HREF":KOMPAS_LINK_HREF,
    "TEXT_CLASS":KOMPAS_TEXT_CLASS,
    "DATE_CLASS":KOMPAS_DATE_CLASS
    }

# configuration of cnn ekonomi site
CNN_URL = cnn_config["url"]
CNN_SEARCH_BAR = cnn_config["search_bar"]
CNN_SEARCH_ICON = cnn_config["search_icon"]
CNN_ANCHOR_TAG = cnn_config["anchor_tag"]
CNN_LINK_HREF = cnn_config["link_href"]
CNN_TEXT_CLASS = cnn_config["text_class"]
CNN_DATE_CLASS =  cnn_config["date_class"]
CNN_CONFIG = {
    "URL":CNN_URL,
    "SEARCH_BAR":CNN_SEARCH_BAR,
    "SEARCH_ICON":CNN_SEARCH_ICON,
    "ANCHOR_TAG":CNN_ANCHOR_TAG,
    "LINK_HREF":CNN_LINK_HREF,
    "TEXT_CLASS":CNN_TEXT_CLASS,
    "DATE_CLASS":CNN_DATE_CLASS
    }

# configuration of DETIK ekonomi site
DETIK_URL = detik_config["url"]
DETIK_SEARCH_BAR = detik_config["search_bar"]
DETIK_SEARCH_ICON = detik_config["search_icon"]
DETIK_ANCHOR_TAG = detik_config["anchor_tag"]
DETIK_LINK_HREF = detik_config["link_href"]
DETIK_TEXT_CLASS = detik_config["text_class"]
DETIK_DATE_CLASS =  detik_config["date_class"]
DETIK_CONFIG = {
    "URL":DETIK_URL,
    "SEARCH_BAR":DETIK_SEARCH_BAR,
    "SEARCH_ICON":DETIK_SEARCH_ICON,
    "ANCHOR_TAG":DETIK_ANCHOR_TAG,
    "LINK_HREF":DETIK_LINK_HREF,
    "TEXT_CLASS":DETIK_TEXT_CLASS,
    "DATE_CLASS":DETIK_DATE_CLASS
    }

# configuration of tempo bisnis site
TEMPO_URL = tempo_config["url"]
TEMPO_SEARCH_BAR = tempo_config["search_bar"]
TEMPO_SEARCH_ICON = tempo_config["search_icon"]
TEMPO_ANCHOR_TAG = tempo_config["anchor_tag"]
TEMPO_LINK_HREF = tempo_config["link_href"]
TEMPO_TEXT_CLASS = tempo_config["text_class"]
TEMPO_DATE_CLASS =  tempo_config["date_class"]
TEMPO_CONFIG = {
    "URL":TEMPO_URL,
    "SEARCH_BAR":TEMPO_SEARCH_BAR,
    "SEARCH_ICON":TEMPO_SEARCH_ICON,
    "ANCHOR_TAG":TEMPO_ANCHOR_TAG,
    "LINK_HREF":TEMPO_LINK_HREF,
    "TEXT_CLASS":TEMPO_TEXT_CLASS,
    "DATE_CLASS":TEMPO_DATE_CLASS
    }

# configuration of CNBC bisnis site
CNBC_URL = cnbc_config["url"]
CNBC_SEARCH_BAR = cnbc_config["search_bar"]
CNBC_SEARCH_ICON = cnbc_config["search_icon"]
CNBC_ANCHOR_TAG = cnbc_config["anchor_tag"]
CNBC_LINK_HREF = cnbc_config["link_href"]
CNBC_TEXT_CLASS = cnbc_config["text_class"]
CNBC_DATE_CLASS =  cnbc_config["date_class"]
CNBC_CONFIG = {
    "URL":CNBC_URL,
    "SEARCH_BAR":CNBC_SEARCH_BAR,
    "SEARCH_ICON":CNBC_SEARCH_ICON,
    "ANCHOR_TAG":CNBC_ANCHOR_TAG,
    "LINK_HREF":CNBC_LINK_HREF,
    "TEXT_CLASS":CNBC_TEXT_CLASS,
    "DATE_CLASS":CNBC_DATE_CLASS
    }

# configuration of LIPUTAN6 bisnis site
LIPUTAN6_URL = liputan6_config["url"]
LIPUTAN6_SEARCH_BAR = liputan6_config["search_bar"]
LIPUTAN6_SEARCH_ICON = liputan6_config["search_icon"]
LIPUTAN6_ANCHOR_TAG = liputan6_config["anchor_tag"]
LIPUTAN6_LINK_HREF = liputan6_config["link_href"]
LIPUTAN6_TEXT_CLASS = liputan6_config["text_class"]
LIPUTAN6_DATE_CLASS =  liputan6_config["date_class"]
LIPUTAN6_CONFIG = {
    "URL":LIPUTAN6_URL,
    "SEARCH_BAR":LIPUTAN6_SEARCH_BAR,
    "SEARCH_ICON":LIPUTAN6_SEARCH_ICON,
    "ANCHOR_TAG":LIPUTAN6_ANCHOR_TAG,
    "LINK_HREF":LIPUTAN6_LINK_HREF,
    "TEXT_CLASS":LIPUTAN6_TEXT_CLASS,
    "DATE_CLASS":LIPUTAN6_DATE_CLASS
    }