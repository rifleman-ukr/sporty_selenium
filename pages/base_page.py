from selenium.webdriver.common.by import By

header_selector = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]')
find_button_selector = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[2]/a[1]')


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, page_url):
        self.browser.get(page_url)
        assert self.is_page_open(page_url)

    @property
    def search_button(self):
        return self.find(find_button_selector)

    @property
    def header(self):
        return self.find(header_selector)

    def is_page_scrolled(self):
        return True if self.header.location_once_scrolled_into_view['y'] == -50 else False

    def scroll_page_down(self):
        self.browser.execute_script(f'scrollBy(0, {self.browser.get_window_size()['height']/2})')

    def is_page_open(self, page_url):
        return self.browser.current_url == page_url

    def find(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)
