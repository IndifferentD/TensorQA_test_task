import pytest
import logging
from pages.yandex_home import YandexHomePage
from pages.yandex_search_result import YandexSearchResultPage
from time import sleep
logger = logging.getLogger(__name__)


def test_first_result_is_tensor(browser):
    """Check that first search result is tensor.ru"""
    logger.info('-----Starting test that checks first search result with query "Тензор" is tensor.ru-----')
    yandex_home_page = YandexHomePage(browser)
    yandex_search_result_page = YandexSearchResultPage(browser)

    # 1)	Зайти на https://ya.ru/
    logger.info(f'Step 1: Opening page {yandex_home_page._base_url}')
    try:
        yandex_home_page.go_to_site()
    except Exception:
        pytest.fail(f"failed to load page {yandex_home_page._base_url}")
        raise

    # 2)	Проверить наличия поля поиска
    logger.info(f'Step 2: Checking search field is presented on page')
    assert yandex_home_page.search_field.is_presented(), "search field not found"

    # 3)	Ввести в поиск Тензор
    logger.info('Step 3: entering "Тензор" ин search field')
    yandex_home_page.search_field.send_keys('Тензор')
    sleep(0.3)

    # 4)	Проверить, что появилась таблица с подсказками (suggest)
    logger.info('Step 4: Checking presence of suggests popup table')
    assert yandex_home_page.suggests_popup_container.is_displayed(), "suggests popup container is not visible"

    # 5)	Нажать enter
    logger.info('Step 5: Pressing "Enter" to proceed to search results page')
    yandex_home_page.search_field.press_enter()

    sleep(.2)
    logger.info('Removing yandex browser advertisement if presented')
    # убираем баннер с предложением установки яндекс браузера, т.к. он перекрывает результаты поиска
    yandex_search_result_page.install_browser_suggest_overlay.delete()
    # 6)	Проверить, что появилась страница результатов поиска
    logger.info('Step 6: Checking that search result page has been loaded')
    assert browser.current_url.startswith(yandex_search_result_page._base_url) , "search result page did not appeared"

    # 7)	Проверить 1 ссылка ведет на сайт tensor.ru
    expected_result_url = 'https://tensor.ru/'
    logger.info(f'Step 7: Checking that first link in search results is {expected_result_url}')
    yandex_search_result_page.first_search_result.is_displayed()
    assert yandex_search_result_page.first_search_result.get_attribute('href') == expected_result_url, f"first result is not {expected_result_url}"

    logger.info('-----Test finished-----')
