from app import app
import urllib.request,json
from .models import news

 News= news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
news_base_url = app.config["NEWS_UPDATES_BASE_URL"]