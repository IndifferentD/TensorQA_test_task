from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement(object):
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10

    def __init__(self, locator: tuple[By, str], timeout=10, **kwargs):
        self._timeout = timeout
        self._locator = locator

    def find(self, timeout=10):
        """ Find element on the page. """

        element = None

        try:
            element = self._web_driver.find_element(*self._locator)
        except:
            print('Element not found on the page!')

        return element

    def is_presented(self):
        """ Check that element is presented on the page. """

        element = self.find(timeout=0.1)
        return element is not None

    def is_displayed(self):
        """ Check is the element visible or not. """

        element = self.find(timeout=0.1)

        if element:
            return element.is_displayed()

        return False

    def get_attribute(self, attr_name):
        """ Get attribute of the element. """

        element = self.find()

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
            print('Element not clickable!')

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

        if element:
            element.send_keys(keys)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def press_enter(self):
        self.send_keys(Keys.RETURN)

    def get_tag_name(self):
        element = self.find(timeout=0.1)

        if element:
            return element.tag_name

        return False

    def is_image_displayed(self):
        element = self.find(timeout=0.1)

        if element and element.tag_name == 'img':
            return self._web_driver.execute_script("return arguments[0].naturalWidth > 0;", self.find())

        return False

