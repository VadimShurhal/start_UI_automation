import allure
import pytest
from selene import browser


#Method to add screenshot to allure report
def pytest_exception_interact(node, call, report):
    driver = node.instance.driver
    allure.attach(
        name='Скриншот',
        body=browser.driver().get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG,
    )


