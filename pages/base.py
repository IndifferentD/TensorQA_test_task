
class WebPage(object):
    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self._base_url = url

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name)._set_value(self._web_driver, value)
        else:
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def go_to_site(self):
        return self._web_driver.get(self._base_url)
