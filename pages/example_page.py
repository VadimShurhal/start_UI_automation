import allure
from selene import browser


@allure.step("Open browser on page stackoverflow.com ")
def open_browser():
    print('Hello')
    browser.open_url('https://stackoverflow.com')