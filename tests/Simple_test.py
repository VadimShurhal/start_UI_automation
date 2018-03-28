import os
import pytest
import allure
from selene import *
from selene import browser
from selene import config
from selene.browsers import BrowserName

from selene.support.jquery_style_selectors import s
from conftest import *
from pages.example_page import open_browser

config.browser_name = BrowserName.CHROME  # Choice browser
config.reports_folder = os.path.join(os.getcwd(), "screenshots") # Sending screenshots to the current directory



@allure.story("Explore Tab")
@allure.feature("Sample suite")
class Test_Simple:
    driver = browser.driver()

    def setup(m):
        print ('\n ****************** START TEST CASE ************** \n')

    def teardown(m):
        print ('\n ****************** END TEST KEYS ***************** \n')

    @allure.step("Test case 1")
    @allure.testcase("http://my.tms.org/TESTCASE-1")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_simple(self):
        print('test 1 ')
        open_browser()

    @allure.step("Test case 2")
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_simple_1(self):
        print('test 2 ')
        open_browser()

    @allure.step("Test case 3")
    @allure.testcase("http://my.tms.org/TESTCASE-3")
    @allure.severity(allure.severity_level.NORMAL)
    def test_simple_2(self):
        open_browser()
        print('test 3 ')
        print (browser.driver().title)
        s('error').click()
