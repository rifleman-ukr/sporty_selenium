import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

root_selector = (By.CSS_SELECTOR, '#root[data-a-page-events-submitted]')


class StreamerPage(BasePage):
    def __init__(self, browser, test_data):
        super().__init__(browser)
        self.page_url = re.compile(f'{test_data['main_page_url']}.*/home')

    def wait_page_loaded(self):
        if self.page_url.match(self.browser.current_url):
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(root_selector))
            time.sleep(2)
            """ Unfortunately I couldn't manage to find an effective way to ensure that the page is fully 
            loaded due to lack of time, that's why time.sleep() is used as an emergency solution"""
            return self.browser.current_url

