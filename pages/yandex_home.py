from selenium.webdriver.common.by import By
from page_object_methods import get_web_element


class YandexHomePage:
    URL = 'https://ya.ru/'

    # Locators
    SEARCH_FIELD = (By.ID, 'text')
    SUGGESTS_POPUP_CONTAINER = (By.CLASS_NAME, 'mini-suggest__popup-container')
    # Меню ya сервисов
    ALL_SERVICES_BUTTON = (By.CSS_SELECTOR, 'a[title="Все сервисы"]')
    # IMAGES_DIV = (By.CSS_SELECTOR, 'div[data-id="images"]')
    # IMAGES_SPAN_DIV = (By.CSS_SELECTOR, 'span.services-more-popup__item > div[data-id="images"]')
    IMAGES_A = (By.CSS_SELECTOR, 'a[aria-label="Картинки"]')

    # Прочие локаторы
    # FIRST_A_IN_ELEMENT = (By.TAG_NAME, 'a')
    # UPPER_ELEMENT = (By.XPATH, '..')

    def __init__(self, driver):
        self.driver = driver
        self._search_field=False    # TODO: создать для элементов страницы класс WebElement, чтобы их инициализация
        # происходила только в момент обращения к свойству класса PageObject?

    @property
    def search_field(self):
        self._search_field=get_web_element(self.driver, self.SEARCH_FIELD)
        return self._search_field

    @search_field.setter
    def search_field(self,chr):
        self._search_field.send_keys(chr)


    def get_suggests_popup_container(self):
        return get_web_element(self.driver, self.SUGGESTS_POPUP_CONTAINER)

    def get_all_service_button(self):
        return get_web_element(self.driver, self.ALL_SERVICES_BUTTON)

    # def get_images_div(self):
    #     return get_web_element(self.driver, self.IMAGES_SPAN_DIV)
    #
    # def get_images_span(self):
    #     return get_web_element(self.get_images_div(), self.UPPER_ELEMENT)
    #
    # def get_images_a(self):
    #     if self.get_images_span() is not None:
    #         return get_web_element(self.get_images_span(), self.FIRST_A_IN_ELEMENT)
    #     else:
    #         return ''


    def get_images_a(self):
        return get_web_element(self.driver, self.IMAGES_A)

    def click_inside_search_bar(self):
        self.get_search_field().click()

    def click_images_button(self):
        self.get_images_a().click()

