from utils import wait_until, make_screenshot


def test_01_open_main_page(main_page):
    main_page.open()
    assert main_page.search_button.is_displayed(), 'Search button should be displayed'


def test_02_click_search_button(main_page, search_page):
    main_page.open()
    main_page.search_button.click()
    assert search_page.is_open, 'Search page should be open'
    assert search_page.search_input.is_displayed(), 'Search input should be displayed'


def test_03_input_search_text(search_page, category_page, test_data):
    search_page.open()
    search_page.search(test_data['search_text'])[0].click()
    assert wait_until(lambda: category_page.is_open), 'Category page should open'


def test_04_scroll_down(category_page):
    category_page.open()
    assert not category_page.is_page_scrolled(), 'Header should be displayed before scroll down'
    category_page.scroll_page_down()
    assert wait_until(lambda: category_page.is_page_scrolled()), 'Header should not be displayed after scroll down'
    category_page.scroll_to_element()


def test_05_select_streamer(browser, category_page, streamer_page):
    category_page.open_streamer_page()
    assert streamer_page.wait_page_loaded(), 'Streamer page should be loaded'
    make_screenshot(browser)
