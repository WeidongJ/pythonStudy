from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class UrlTitleTests(TestCase):
    '''Base url test'''
    def test_url_title(self):
        browser = webdriver.Firefox()
        browser.get('http://localhost:8000')
        assert 'Django' in browser.title
        browser.quit()
