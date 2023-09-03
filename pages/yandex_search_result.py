from selenium.webdriver.common.by import By
from pages.base import WebPage
from pages.elements import WebElement

class YandexSearchResultPageLocators:
    """ Yandex search service page locators"""
    # FIRST_RESULT_A=(By.XPATH,'//li[@data-first-snippet="true"]//a[1]') # не актуально на 03.09.2023
    FIRST_RESULT_A = (By.XPATH, '//ul[@id="search-result"]/li/div/div/a')
    INSTALL_BROWSER_SUGGEST_OVERLAY=(By.CLASS_NAME,'DistrSplashscreen')

class YandexSearchResultPage(WebPage):
    """ Yandex search service page WebPage class"""
    def __init__(self, web_driver):
        self._base_url = 'https://ya.ru/search/'
        super().__init__(web_driver,self._base_url)

    first_search_result=WebElement(YandexSearchResultPageLocators.FIRST_RESULT_A,name='first_search_result')
    install_browser_suggest_overlay=WebElement(YandexSearchResultPageLocators.INSTALL_BROWSER_SUGGEST_OVERLAY,name='install_browser_suggest_overlay')




