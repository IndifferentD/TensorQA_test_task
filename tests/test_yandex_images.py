import pytest
from pages.yandex_home import YandexHomePage
from pages.yandex_images import YandexImagesPage
from time import sleep
from selenium.webdriver import ActionChains


def test_yandex_images_category(browser):
    """Check that yandex images category works correctly"""

    yandex_home_page = YandexHomePage(browser)
    yandex_images_page = YandexImagesPage(browser)

    # Опытным путём было выявлено, что после райт-клика по изображению
    # аттрибут src в классе img class="MMImage-Origin" меняется с сгенерированной яндексом ссылки для превью
    # на ссылку, ведущую на оригинальное изображение
    # поэтому был добавлен модуль, позволяющий использовать клик правой кнопкой мышки
    # т.к. в качестве проверки идентичности изображений было принято сравнение ссылок на них
    actionChains = ActionChains(browser)

    # 1)	Зайти на https://ya.ru/
    try:
        browser.get(yandex_home_page.URL)
    except Exception as err:
        pytest.fail(f"Не удалось загрузить страницу {yandex_home_page.URL}")

    # 2)	Проверить, что кнопка меню присутствует на странице
    # assert yandex_home_page.get_search_field() is not None
    yandex_home_page.search_field.click()
    assert yandex_home_page.get_all_service_button() is not None
    sleep(0.3)

    # 3)	Открыть меню, выбрать “Картинки”
    yandex_home_page.get_all_service_button().click()
    sleep(0.3)


    yandex_home_page.get_images_a().click()
    sleep(0.3)

    # 4)	Проверить, что перешли на url https://yandex.ru/images/

    # после открытия вкладки методом click необходимо вручную менять current_window_handle
    # чтобы иметь возможност работать с элементами на странице
    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == yandex_images_page.URL

    # Фиксируем поисковый запрос самой популярной категории
    most_popular_category_search_text = yandex_images_page.get_most_popular_category_div_container_text()

    # 5)	Открыть первую категорию
    yandex_images_page.get_category_a(yandex_images_page.get_most_popular_category_div_container()).click()
    sleep(.3)

    # 6)	Проверить, что название категории отображается в поле поиска
    assert yandex_images_page.get_search_field_text() == most_popular_category_search_text

    # 7)	Открыть 1 картинку
    yandex_images_page.get_first_image().click()
    sleep(.3)

    # 8)	Проверить, что картинка открылась
    actionChains.context_click(yandex_images_page.get_full_image_origin()).perform()
    first_image_url = yandex_images_page.get_full_image_origin().get_attribute('src')
    assert yandex_images_page.get_full_image_preview().is_displayed()

    # 9)	Нажать кнопку вперед
    yandex_images_page.get_next_button_div().click()
    sleep(.3)

    # 10.	Проверить, что картинка сменилась
    actionChains.context_click(yandex_images_page.get_full_image_origin()).perform()
    assert yandex_images_page.get_full_image_preview().is_displayed() and first_image_url != yandex_images_page.get_full_image_origin().get_attribute(
        'src')

    # 11.	Нажать назад
    yandex_images_page.get_prev_button_div().click()
    sleep(.3)

    # 12.	Проверить, что картинка осталась из шага 8
    actionChains.context_click(yandex_images_page.get_full_image_origin()).perform()
    assert yandex_images_page.get_full_image_preview().is_displayed() and first_image_url == yandex_images_page.get_full_image_origin().get_attribute(
        'src')
