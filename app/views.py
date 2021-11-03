from flask import render_template
from app import app
from flask_bootstrap import Bootstrap
from .request import get_news, get_sources 

# News
@app.route('/')
def index():

    '''
    news root page function that returns the index page and its data
    '''

    # Getting News, sources
    title= 'News Updates'
    country_news = get_news('us')
    news_source = get_sources()
    # return render_template('index.html', title = title, country = country_news, sources = news_source)
    return "Hello world"