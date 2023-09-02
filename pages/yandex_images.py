from selenium.webdriver.common.by import By

from page_object_methods import get_web_element


class YandexImagesPage:
    URL = 'https://ya.ru/images/'
    # Images search elements
    POPULAR_REQUEST_LIST_DIV = (By.CLASS_NAME, 'PopularRequestList')
    MOST_POPULAR_REQUEST = (By.CLASS_NAME, 'PopularRequestList-Item')
    REQUEST_SEARCH_TEXT = (By.CLASS_NAME, 'PopularRequestList-SearchText')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="text"]')
    FIRST_IMAGE = (By.CLASS_NAME, 'serp-item__link')
    # Full image view elements
    FULL_IMAGE_ORIGIN = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    FULL_IMAGE_PREVIEW = (By.CSS_SELECTOR, 'img.MMImage-Preview')
    NEXT_BUTTON = (By.CLASS_NAME, 'CircleButton-Icon')
    NEXT_BUTTON = (By.CSS_SELECTOR,
                   'div.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button.MediaViewer_theme_fiji-Button.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext')
    PREV_BUTTON = (By.CSS_SELECTOR,
                   'div.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button.MediaViewer_theme_fiji-Button.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'div[class*="MediaViewer-ButtonNext"]')
    PREV_BUTTON = (By.CSS_SELECTOR, 'div[class*="MediaViewer-ButtonPrev"]')

    FIRST_A_IN_ELEMENT = (By.TAG_NAME, 'a')

    def __init__(self, driver):
        self.driver = driver

    def get_most_popular_category_div_container(self):
        return get_web_element(self.driver, self.MOST_POPULAR_REQUEST)

    def get_most_popular_category_div_container_text(self):
        return get_web_element(self.get_most_popular_category_div_container(), self.REQUEST_SEARCH_TEXT).text

    def get_search_field(self):
        return get_web_element(self.driver, self.SEARCH_FIELD)

    def get_search_field_text(self):
        return self.get_search_field().get_attribute('value')

    def get_category_a(self, category):
        return get_web_element(category, self.FIRST_A_IN_ELEMENT)

    def get_first_image(self):
        return get_web_element(self.driver, self.FIRST_IMAGE)

    def get_full_image_origin(self):
        return get_web_element(self.driver, self.FULL_IMAGE_ORIGIN)

    def get_full_image_preview(self):
        return get_web_element(self.driver, self.FULL_IMAGE_PREVIEW)

    def get_next_button_div(self):
        return get_web_element(self.driver, self.NEXT_BUTTON)

    def get_prev_button_div(self):
        return get_web_element(self.driver, self.PREV_BUTTON)

    # SEARCH_FIELD = (By.ID, 'text')
    # SUGGESTS_POPUP_CONTAINER = (By.CLASS_NAME, 'mini-suggest__popup-container')
    # ALL_SERVICES_BUTTON = (By.CSS_SELECTOR, 'a[title="Все сервисы"]')
    # IMAGES_DIV = (By.CSS_SELECTOR, 'div[data-id="images"')
    # IMAGES_SPAN = (By.CSS_SELECTOR, 'span.services-more-popup__item > div[data-id="images"]')
    # FIRST_A_IN_ELEMENT = (By.TAG_NAME, 'a')
    # UPPER_ELEMENT=(By.XPATH,'..')
