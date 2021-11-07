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
    
def get_sources():
    '''
    Function that gets the json response to url request
    '''
    # get_news_url = base_url.format(category,api_key)              #new
    get_sources_url= 'https://newsapi.org/v2/sources?apiKey=4c6387d3b12945de99414364a18d6452'
    # print(get_source_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category=source_item.get('category')
        if id:
            source_object = Source(id,name,description,url,category)
            source_results.append(source_object)

    return source_results

