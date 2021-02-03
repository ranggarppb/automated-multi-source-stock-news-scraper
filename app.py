from news_scraper import get_news
from globar_var import KOMPAS_URL, KOMPAS_FOCUSED_SEARCH_XPATH, KOMPAS_FOCUSED_SUBMIT_XPATH, KOMPAS_FOCUSED_LINK_XPATH, KOMPAS_FOCUSED_LINK_HREF, KOMPAS_FOCUSED_TEXT_CLASS, CNN_URL, CNN_FOCUSED_XPATH, CNN_FOCUSED_HREF, CNN_FOCUSED_CLASS

if __name__ == "__main__":
    
    news = {}
    stock = 'BBCA'

    # get money kompas news
    kompas_news = get_news(KOMPAS_URL, KOMPAS_FOCUSED_SEARCH_XPATH, stock , KOMPAS_FOCUSED_SUBMIT_XPATH, 
    KOMPAS_FOCUSED_LINK_XPATH, KOMPAS_FOCUSED_LINK_HREF, KOMPAS_FOCUSED_TEXT_CLASS)
    news.update({"money_kompas":kompas_news})
    # get cnn ekonomi news
    # cnn_news = get_news(CNN_URL, CNN_FOCUSED_XPATH, CNN_FOCUSED_HREF, CNN_FOCUSED_CLASS)
    # news.update({"cnn_ekonomi":cnn_news})
    # print(news["money_kompas"])
    # print(news["cnn_ekonomi"])