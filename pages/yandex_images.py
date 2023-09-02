from selenium.webdriver.common.by import By
from pages.base import WebPage
from pages.elements import WebElement


class YandexImagesPageLocators:
    # Images search elements
    MOST_POPULAR_REQUEST = (By.XPATH, '//div[@class="PopularRequestList"]//div[1]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="text"]')
    FIRST_IMAGE_IN_SEARCH_RESULTS = (By.XPATH, '//div[contains(@class, "serp-list")]//div[1]//div[1]//a[1]')
    # Full image view elements
    FULL_IMAGE_PREVIEW = (By.CSS_SELECTOR, 'img.MMImage-Preview')
    FULL_IMAGE_ORIGIN = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'div[class*="MediaViewer-ButtonNext"]')
    PREV_BUTTON = (By.CSS_SELECTOR, 'div[class*="MediaViewer-ButtonPrev"]')


class YandexImagesPage(WebPage):

    def __init__(self, web_driver):
        self._base_url = 'https://ya.ru/images/'
        super().__init__(web_driver, self._base_url)

    most_popular_category = WebElement(YandexImagesPageLocators.MOST_POPULAR_REQUEST)
    search_field = WebElement(YandexImagesPageLocators.SEARCH_FIELD)
    first_image_in_search_results = WebElement(YandexImagesPageLocators.FIRST_IMAGE_IN_SEARCH_RESULTS)
    button_next = WebElement(YandexImagesPageLocators.NEXT_BUTTON)
    button_prev = WebElement(YandexImagesPageLocators.PREV_BUTTON)
    # Превью картинки яндекса для проверки is_image_displayed()
    image_preview = WebElement(YandexImagesPageLocators.FULL_IMAGE_PREVIEW)
    # <img> для получения src ссылки на оригинальное изображения
    image_origin = WebElement(YandexImagesPageLocators.FULL_IMAGE_ORIGIN)
