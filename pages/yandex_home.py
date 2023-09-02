from selenium.webdriver.common.by import By
from pages.base import WebPage
from pages.elements import WebElement


class YandexHomePageLocators:
    SEARCH_FIELD = (By.ID, 'text')
    SUGGESTS_POPUP_CONTAINER = (By.CLASS_NAME, 'mini-suggest__popup-container')
    # Меню yandex сервисов
    ALL_SERVICES_BUTTON = (By.CSS_SELECTOR, 'a[title="Все сервисы"]')
    IMAGES_SERVICE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Картинки"]')


class YandexHomePage(WebPage):

    def __init__(self, web_driver):
        self._base_url = 'https://ya.ru/'
        super().__init__(web_driver, self._base_url)

    search_field = WebElement(YandexHomePageLocators.SEARCH_FIELD)
    suggests_popup_container = WebElement(YandexHomePageLocators.SUGGESTS_POPUP_CONTAINER)
    all_services_button = WebElement(YandexHomePageLocators.ALL_SERVICES_BUTTON)
    images_service_button = WebElement(YandexHomePageLocators.IMAGES_SERVICE_BUTTON)
