"""

Collection of configuration variables

"""
from utils import config_reader
CONFIG_FILE="config.ini"

config_news_scraper = config_reader(CONFIG_FILE, section="news_scraper")
config_kompas = config_reader(CONFIG_FILE, section="kompas_config")

# configuration of news scraper
DRIVER_PATH = config_news_scraper["driver_path"]

# configuration of money kompas site
KOMPAS_URL = config_kompas["url"]
KOMPAS_FOCUSED_HREF = config_kompas["focused_href"]
KOMPAS_FOCUSED_CLASS = config_kompas["focused_class"]
