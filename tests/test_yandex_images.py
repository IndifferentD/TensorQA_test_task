import pytest
import logging
from pages.yandex_home import YandexHomePage
from pages.yandex_images import YandexImagesPage
from time import sleep

logger = logging.getLogger(__name__)


# TODO: необходимо добавить методы ожидания перед кликом/готовности страницы
def step_sleep():
    sleep(.5)


def test_yandex_images_category(browser):
    """Check that yandex images category works correctly"""
    logger.info('-----Starting test that checks yandex images category works correctly-----')
    yandex_home_page = YandexHomePage(browser)
    yandex_images_page = YandexImagesPage(browser)

    # 1)	Зайти на https://ya.ru/
    logger.info(f'Step 1: Opening page {yandex_home_page._base_url}')
    try:
        yandex_home_page.go_to_site()
    except Exception as err:
        pytest.fail(f"Не удалось загрузить страницу {yandex_home_page._base_url}")

    # 2)	Проверить, что кнопка меню присутствует на странице
    logger.info(f'Step 2: Checking presence of menu button')
    yandex_home_page.search_field.click()
    assert yandex_home_page.all_services_button.is_presented(), "Service menu Button not found"
    # assert False, "Service menu Button not found"
    step_sleep()

    # 3)	Открыть меню, выбрать “Картинки”
    yandex_home_page.all_services_button.click()
    step_sleep()
    logger.info('Step 3: Clicking images category button')
    yandex_home_page.images_service_button.click()
    step_sleep()

    # 4)	Проверить, что перешли на url https://yandex.ru/images/
    logger.info(f'Step 4: Checking current url is {yandex_images_page._base_url}')
    # после открытия вкладки методом click необходимо вручную менять current_window_handle
    # чтобы иметь возможност работать с элементами на странице
    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == yandex_images_page._base_url, f"Current URL is not {yandex_images_page._base_url}"

    # Фиксируем поисковый запрос самой популярной категории
    most_popular_category_search_text = yandex_images_page.most_popular_category.get_attribute('data-grid-text')

    # 5)	Открыть первую категорию
    logger.info('Step 5: Opening most popular category')
    yandex_images_page.most_popular_category.click()
    step_sleep()

    # 6)	Проверить, что название категории отображается в поле поиска
    logger.info(f'Step 6: Checking that most popular category "{most_popular_category_search_text}" is in search field')
    assert yandex_images_page.search_field.get_attribute(
        'value') == most_popular_category_search_text, f"'{most_popular_category_search_text}' not found in search field"

    # 7)	Открыть 1 картинку
    logger.info('Step 7: Opening 1st image in category')
    yandex_images_page.first_image_in_search_results.click()
    step_sleep()

    # 8)	Проверить, что картинка открылась
    logger.info('Step 8: Checking image has been loaded')
    assert yandex_images_page.image_preview.is_image_displayed(), "Image is not displayed"
    # Опытным путём было выявлено, что после райт-клика по изображению - аттрибут src в элемнте img class="MMImage-Origin"
    # меняется с сгенерированной яндексом ссылки для превью на ссылку, ведущую на оригинальное изображение.
    # эта ссылка необходима для сравнения идентичности изображений в одном из следующих шагов
    yandex_images_page.image_origin.right_mouse_click()
    first_image_url = yandex_images_page.image_origin.get_attribute('src')

    # 9)	Нажать кнопку вперед
    logger.info('Step 9: Pressing next image button')
    yandex_images_page.button_next.click()
    step_sleep()
    # 10.	Проверить, что картинка сменилась
    logger.info('Step 10: Checking image has been changed')
    yandex_images_page.image_origin.right_mouse_click()
    assert yandex_images_page.image_preview.is_image_displayed() and first_image_url != yandex_images_page.image_origin.get_attribute(
        'src'), "Image has not been changed"

    # 11.	Нажать назад
    logger.info('Step 11: Pressing previous image button')
    yandex_images_page.button_prev.click()
    step_sleep()

    # 12.	Проверить, что картинка осталась из шага 8
    logger.info('Step 12: Checking that current image is from step 8')
    yandex_images_page.image_origin.right_mouse_click()
    assert yandex_images_page.image_preview.is_image_displayed() and first_image_url == yandex_images_page.image_origin.get_attribute(
        'src'), "Image differs from image previously loaded in step 8"

    logger.info('-----Test finished-----')
