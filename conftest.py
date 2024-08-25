import json
from os import path

import pytest
from selenium import webdriver

from pages.category_page import CategoryPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage


@pytest.fixture(scope='session')
def browser(test_data):
    chrome_options = webdriver.ChromeOptions()
    if test_data['device_name']:
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": test_data["device_name"]})
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser


@pytest.fixture(scope="session")
def test_data():
    with open(path.join(path.dirname(path.abspath(__file__)), 'test_data.json')) as test_data_vars:
        return json.load(test_data_vars)


@pytest.fixture(scope='session')
def main_page(browser, test_data):
    return MainPage(browser, test_data)


@pytest.fixture(scope='session')
def search_page(browser, test_data):
    return SearchPage(browser, test_data)


@pytest.fixture(scope='session')
def category_page(browser, test_data):
    return CategoryPage(browser, test_data)


@pytest.fixture(scope='session')
def streamer_page(browser, test_data):
    return StreamerPage(browser, test_data)
