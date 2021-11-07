class Config:
    '''
    General configuration parent class
    '''
    NEWS_UPDATES_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category={}?api_key={}'
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=?api_key{}'
    NEWS_API_KEY = '0de28d09fb894c7bbc3d053f21fdbc4f'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True