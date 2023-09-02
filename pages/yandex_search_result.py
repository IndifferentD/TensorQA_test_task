from selenium.webdriver.common.by import By
from page_object_methods import get_web_element


class YandexSearchResultPage:
    FIRST_RESULT_LI = (By.CSS_SELECTOR, 'li[data-first-snippet="true"]')
    FIRST_A_IN_ELEMENT = (By.TAG_NAME, 'a')
    RESULTS_UL = (By.ID, 'search-result')
    URL = 'https://ya.ru/search/'

    def __init__(self, driver):
        self.driver = driver

    def fill_search_input(self, query: str):
        self.search_input.send_keys(query)

    def get_search_result_ul(self):
        return get_web_element(self.driver, self.FIRST_RESULT_LI)

    def get_first_result_url(self):
        result_first_li_element = get_web_element(self.driver, self.FIRST_RESULT_LI)
        if result_first_li_element is not None:
            first_a_in_element = get_web_element(result_first_li_element, self.FIRST_A_IN_ELEMENT)
            a_url = first_a_in_element.get_attribute('href')
            return a_url
        else:
            return ''

