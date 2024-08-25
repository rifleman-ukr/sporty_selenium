import os.path
import time


def wait_until(condition, timeout=5, period=0.25, *args, **kwargs):
    wait_timeout = time.time() + timeout
    while time.time() < wait_timeout:
        if condition(*args, **kwargs):
            return True
        time.sleep(period)
    return False


def make_screenshot(browser):
    if not os.path.exists('artifacts'):
        os.makedirs('artifacts')
    browser.get_screenshot_as_file(f'artifacts/{time.time()}.png')
