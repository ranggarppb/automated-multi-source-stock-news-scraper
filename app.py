from news_scraper import get_news
from globar_var import KOMPAS_URL, KOMPAS_FOCUSED_HREF, KOMPAS_FOCUSED_CLASS

if __name__ == "__main__":
    
    news = {}

    # get money kompas news
    kompas_news = get_news(KOMPAS_URL, KOMPAS_FOCUSED_HREF, KOMPAS_FOCUSED_CLASS)
    news.update({"money_kompas":kompas_news})

    print(news)