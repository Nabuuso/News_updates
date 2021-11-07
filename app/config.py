import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = '0de28d09fb894c7bbc3d053f21fdbc4f'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
