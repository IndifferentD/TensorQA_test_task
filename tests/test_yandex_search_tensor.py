import pytest
from pages.yandex_home import YandexHomePage
from pages.yandex_search_result import YandexSearchResultPage
from selenium.webdriver.common.keys import Keys
from time import sleep


# Определяем функцию-тест test_successful_login, которая принимает фикстуру browser в качестве аргумента
def test_first_result_is_tensor(browser):
    """Check that first search result is tensor.ru"""

    # Создаем экземпляр LoginPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    yandex_home_page = YandexHomePage(browser)
    yandex_search_result_page = YandexSearchResultPage(browser)

    # 1)	Зайти на https://ya.ru/
    try:
        browser.get(yandex_home_page.URL)
    except Exception:
        pytest.fail(f"Не удалось загрузить страницу {yandex_home_page.URL}")
        raise

    # 2)	Проверить наличия поля поиска
    assert yandex_home_page.search_field is not None

    # 3)	Ввести в поиск Тензор
    yandex_home_page.search_field='Тензор'
    sleep(0.3)

    # 4)	Проверить, что появилась таблица с подсказками (suggest)
    assert yandex_home_page.get_suggests_popup_container().is_displayed()

    # 5)	Нажать enter
    yandex_home_page.search_field=Keys.RETURN
    # 6)	Проверить, что появилась страница результатов поиска
    assert browser.current_url.startswith(
        yandex_search_result_page.URL) and yandex_search_result_page.get_search_result_ul().is_displayed()

    # 7)	Проверить 1 ссылка ведет на сайт tensor.ru
    assert yandex_search_result_page.get_first_result_url() == 'https://tensor.ru/'
