from app import app
import urllib.request,json
from .models import news, sources, entertainment

News= news.News
Sources = sources.Sources
Entertainment = entertainment.Entertainment

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
news_base_url = app.config["NEWS_UPDATES_BASE_URL"]

# Getting the sources base url
sources_base_url = app.config["NEWS_SOURCE_BASE_URL"]

# Getting the entertainment news base url
entertainment_base_url = app.config["NEWS_ENTERTAINMENT_BASE_URL"]

def get_news(world):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_base_url.format(world,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news-articles']:
            news_results_list = get_news_response['news-articles']
            news_results = process_newsResults(news_results_list)


    return news_results

def process_newsResults(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = movie_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results