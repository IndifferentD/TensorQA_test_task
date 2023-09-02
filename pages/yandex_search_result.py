from selenium.webdriver.common.by import By
from pages.base import WebPage
from pages.elements import WebElement

class YandexSearchResultPageLocators:
    FIRST_RESULT_A=(By.XPATH,'//li[@data-first-snippet="true"]//a[1]')

class YandexSearchResultPage(WebPage):
    def __init__(self, web_driver):
        self._base_url = 'https://ya.ru/search/'
        super().__init__(web_driver,self._base_url)

    first_search_result=WebElement(YandexSearchResultPageLocators.FIRST_RESULT_A)




