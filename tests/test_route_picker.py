import allure

from data.test_data import (
    ADDRESS_FROM,
    ADDRESS_TO,
    FREE_ROUTE_TEXT,
    ROUTE_MODES,
    ZERO_MINUTES_TEXT,
)
from pages.main_page import MainPage
from pages.route_picker_page import RoutePickerPage


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRoutePicker:

    @allure.title("Блок выбора маршрута появляется после ввода двух адресов")
    def test_route_picker_is_shown(self, driver):
        main_page = MainPage(driver)
        main_page.build_route(ADDRESS_FROM, ADDRESS_TO)

        picker = RoutePickerPage(driver)

        assert picker.is_shown()

    @allure.title("Отображаются три режима маршрута")
    def test_three_route_modes_are_shown(self, driver):
        main_page = MainPage(driver)
        main_page.build_route(ADDRESS_FROM, ADDRESS_TO)

        picker = RoutePickerPage(driver)

        assert picker.mode_names() == ROUTE_MODES

    @allure.title("Для одинаковых адресов маршрут бесплатный и на 0 мин")
    def test_same_addresses_show_free_route(self, driver):
        main_page = MainPage(driver)
        main_page.build_route(ADDRESS_FROM, ADDRESS_FROM)

        picker = RoutePickerPage(driver)

        assert FREE_ROUTE_TEXT in picker.result_text()
        assert ZERO_MINUTES_TEXT in picker.result_duration()