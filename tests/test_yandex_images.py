import pytest
from pages.yandex_home import YandexHomePage
from pages.yandex_images import YandexImagesPage
from time import sleep

# TODO: необходимо добавить методы ожидания перед кликом/готовности страницы
def step_sleep():
    sleep(.5)

def test_yandex_images_category(browser):
    """Check that yandex images category works correctly"""

    yandex_home_page = YandexHomePage(browser)
    yandex_images_page = YandexImagesPage(browser)

    # 1)	Зайти на https://ya.ru/
    try:
        yandex_home_page.go_to_site()
    except Exception as err:
        pytest.fail(f"Не удалось загрузить страницу {yandex_home_page._base_url}")

    # 2)	Проверить, что кнопка меню присутствует на странице
    yandex_home_page.search_field.click()
    assert yandex_home_page.all_services_button.is_presented(), "Service menu Button not found"
    step_sleep()

    # 3)	Открыть меню, выбрать “Картинки”
    yandex_home_page.all_services_button.click()
    step_sleep()
    yandex_home_page.images_service_button.click()
    step_sleep()

    # 4)	Проверить, что перешли на url https://yandex.ru/images/

    # после открытия вкладки методом click необходимо вручную менять current_window_handle
    # чтобы иметь возможност работать с элементами на странице
    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == yandex_images_page._base_url, f"Current URL is not {yandex_images_page._base_url}"

    # Фиксируем поисковый запрос самой популярной категории
    most_popular_category_search_text = yandex_images_page.most_popular_category.get_attribute('data-grid-text')

    # 5)	Открыть первую категорию
    yandex_images_page.most_popular_category.click()
    step_sleep()

    # 6)	Проверить, что название категории отображается в поле поиска
    assert yandex_images_page.search_field.get_attribute(
        'value') == most_popular_category_search_text, f"'{most_popular_category_search_text}' not found in search field"

    # 7)	Открыть 1 картинку
    yandex_images_page.first_image_in_search_results.click()
    step_sleep()

    # 8)	Проверить, что картинка открылась
    assert yandex_images_page.image_preview.is_image_displayed(), "Image is not displayed"
    # Опытным путём было выявлено, что после райт-клика по изображению
    # аттрибут src в классе img class="MMImage-Origin" меняется с сгенерированной яндексом ссылки для превью
    # на ссылку, ведущую на оригинальное изображение
    # т.к. в качестве проверки идентичности изображений было принято сравнение ссылок на них
    yandex_images_page.image_origin.right_mouse_click()
    first_image_url = yandex_images_page.image_origin.get_attribute('src')

    # 9)	Нажать кнопку вперед
    yandex_images_page.button_next.click()
    step_sleep()
    # 10.	Проверить, что картинка сменилась
    yandex_images_page.image_origin.right_mouse_click()
    assert yandex_images_page.image_preview.is_image_displayed() and first_image_url != yandex_images_page.image_origin.get_attribute(
        'src'), "Image has not been changed"

    # 11.	Нажать назад
    yandex_images_page.button_prev.click()
    step_sleep()

    # 12.	Проверить, что картинка осталась из шага 8
    yandex_images_page.image_origin.right_mouse_click()
    assert yandex_images_page.image_preview.is_image_displayed() and first_image_url == yandex_images_page.image_origin.get_attribute(
        'src'), "Image differs from image previously loaded in step 8"
