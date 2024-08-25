from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, test_data):
        super().__init__(browser)
        self.page_url = test_data['main_page_url']

    def open(self):
        self.open_page(self.page_url)

    @property
    def is_open(self):
        return self.is_page_open(self.page_url)
