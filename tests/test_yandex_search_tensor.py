import pytest
from pages.yandex_home import YandexHomePage
from pages.yandex_search_result import YandexSearchResultPage
from time import sleep



def test_first_result_is_tensor(browser):
    """Check that first search result is tensor.ru"""

    yandex_home_page = YandexHomePage(browser)
    yandex_search_result_page = YandexSearchResultPage(browser)

    # 1)	Зайти на https://ya.ru/
    try:
        yandex_home_page.go_to_site()
    except Exception:
        pytest.fail(f"failed to load page {yandex_home_page.base_url}")
        raise

    # 2)	Проверить наличия поля поиска
    assert yandex_home_page.search_field.is_presented(), "search field not found"

    # 3)	Ввести в поиск Тензор
    yandex_home_page.search_field.send_keys('Тензор')
    sleep(0.3)

    # 4)	Проверить, что появилась таблица с подсказками (suggest)
    assert yandex_home_page.suggests_popup_container.is_displayed(), "suggests popup container is not visible"

    # 5)	Нажать enter
    yandex_home_page.search_field.press_enter()
    # 6)	Проверить, что появилась страница результатов поиска
    assert browser.current_url.startswith(yandex_search_result_page._base_url) and \
           yandex_search_result_page.first_search_result.is_displayed(), "search result page did not appeared"

    # 7)	Проверить 1 ссылка ведет на сайт tensor.ru
    expected_result_url = 'https://tensor.ru/'
    assert yandex_search_result_page.first_search_result.get_attribute('href') == expected_result_url, f"first result is not {expected_result_url}"
