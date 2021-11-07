import urllib.request
import json
from .models import Source, Articles


api_key = ''

base_url_sources = None

base_url_articles = None


def configure_request(app):
    global api_key, base_url_sources, base_url_articles
    base_url_sources = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']