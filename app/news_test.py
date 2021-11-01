import unittest
from app.request import News
from models import news
News = news.News

class newsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_updates= News('miguna miguna set to return', '11/1/2021', 'https://nation.africa/kenya/miguna-miguna-26916')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.news_updates,News))


if __name__ == '__main__':
    unittest.main()