from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import wait_until

search_input_selector = (By.TAG_NAME, 'input')
quick_search_results_selector = (By.TAG_NAME, 'li')


class SearchPage(BasePage):
    def __init__(self, browser, test_data):
        super().__init__(browser)
        self.page_url = f'{test_data['main_page_url']}search'

    def open(self):
        self.open_page(self.page_url)

    def search(self, text):
        self.search_input.send_keys(text)
        wait_until(lambda: len(self.quick_search_results) > 1)
        return self.find_elements(quick_search_results_selector)


    @property
    def is_open(self):
        return self.browser.current_url == self.page_url

    @property
    def search_input(self):
        return self.find(search_input_selector)

    @property
    def quick_search_results(self):
        return self.find_elements(quick_search_results_selector)
