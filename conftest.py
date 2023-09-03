import pytest

from selenium import webdriver

import logging

disable_loggers = ['selenium.webdriver.common.selenium_manager', 'urllib3.connectionpool',
                   'selenium.webdriver.remote.remote_connection','selenium.webdriver.common.service']


def pytest_configure():
    for logger_name in disable_loggers:
        logging.getLogger(logger_name).level = logging.WARNING


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
