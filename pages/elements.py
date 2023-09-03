from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class WebElement(object):
    """ Base class for web elements"""
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _name = None  # Именной идентификатор для удобства логгирования на уровне DEBUG

    def __init__(self, locator: tuple[By, str], timeout=10, name=None, **kwargs):
        self._timeout = timeout
        self._locator = locator
        self._name = name
        logger.debug(f'Created instance of [{self.__class__.__name__}] with name [{self._name}] and locator [{self._locator}]')
    def find(self, timeout=10):
        """ Find element on the page. """

        element = None
        logger.debug(
            f'[{self.__class__.__name__}] Searching for element [{self._name}] using locator {self._locator} on page {self._web_driver.current_url}')
        try:
            element = self._web_driver.find_element(*self._locator)
        except:
            logger.error(
                f'[{self.__class__.__name__}] Element [{self._name}] with locator {self._locator} not found on page {self._web_driver.current_url}')

        return element

    def is_presented(self):
        """ Check that element is presented on the page. """

        element = self.find(timeout=0.1)
        return element is not None

    def is_displayed(self):
        """ Check is the element visible or not. """

        element = self.find(timeout=0.5)

        if element:
            return element.is_displayed()

        return False

    def get_attribute(self, attr_name):
        """ Get attribute of the element. """

        element = self.find()
        logger.debug(f'[{self.__class__.__name__}]  Getting attribute "{attr_name}" of [{self._name}]')
        if element:
            return element.get_attribute(attr_name)

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Wait until the element will be ready for click. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            logger.error(
                f'[{self.__class__.__name__}] Element with locator {self._locator} is not clickable on page {self._web_driver.current_url}')

        # if check_visibility:
        #     self.wait_until_not_visible()

        return element

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Wait and click the element. """

        # element = self.find()
        element = self.wait_to_be_clickable()
        if element:
            element.click()
        else:
            logger.error(f'[{self.__class__.__name__}] Element [{self._name}] with locator {self._locator} is not found on page {self._web_driver.current_url}')
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def right_mouse_click(self):
        """ Click right mouse button on the element. """

        element = self.find()

        if element:
            action = ActionChains(self._web_driver)
            action.context_click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def send_keys(self, keys):
        """ Send keys to the element. """

        element = self.find()
        logger.debug(f'[{self.__class__.__name__}] Entering "{keys}" into element [{self._name}]')
        if element:
            element.send_keys(keys)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def press_enter(self):
        """ Press enter key (Send \ue006) """
        logger.debug(f'[{self.__class__.__name__}] Pressing "Enter" onto element [{self._name}]')
        self.send_keys(Keys.RETURN)

    def get_tag_name(self):
        """ Get element tag """
        element = self.find(timeout=0.1)

        if element:
            return element.tag_name

        return False

    def is_image_displayed(self):
        """ is_displayed method for images (checks for width of image) """
        element = self.find(timeout=0.1)

        if element and element.tag_name == 'img':
            return self._web_driver.execute_script(
                "return arguments[0].complete " + "&& typeof arguments[0].naturalWidth != \"undefined\" " + "&& arguments[0].naturalWidth > 0",
                element)

        return False

    def delete(self):
        """ Deletes element from the page (using JS). """
        element = self.find()
        logger.debug(f'[{self.__class__.__name__}]  Deleting element [{self._name}] from page {self._web_driver.current_url} using JS]')
        # Delete element:
        self._web_driver.execute_script("arguments[0].remove();", element)
