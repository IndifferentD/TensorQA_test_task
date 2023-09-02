from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Общие методы для классов PageObject

def get_web_element(target_DOM, element_locator: tuple[By, str]):
    """
    :param target_DOM: WebElement/driver
    :param element_locator: кортеж вида (selenium.webdriver.common.by.By, идентификатор локатора)
    :return: Возвращает элемент при его нахождении, в противном случае - None
    """
    try:
        return target_DOM.find_element(*element_locator)
    except NoSuchElementException:
        # TODO: Добавить логгирование
        raise
        # return None
    else:
        raise
