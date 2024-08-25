from selenium.webdriver.common.by import By

from pages.base_page import BasePage

current_streams_selector = (By.TAG_NAME, 'article')
stream_selector = (By.TAG_NAME, 'a')


class CategoryPage(BasePage):
    def __init__(self, browser, test_data):
        super().__init__(browser)
        self.page_url = \
            f"{test_data['main_page_url']}directory/category/{test_data['search_text'].lower().replace(' ', '-')}"

    def open(self):
        self.open_page(self.page_url)

    def scroll_to_element(self, element=-1):
        return self.current_streams[element].location_once_scrolled_into_view

    @property
    def is_open(self):
        return self.is_page_open(self.page_url)

    @property
    def current_streams(self):
        return self.find_elements(current_streams_selector)

    def open_stream(self, n):
        return self.current_streams[n].click()

    def open_streamer_page(self, n=-1):
        self.current_streams[n].find_elements(*stream_selector)[1].click()
