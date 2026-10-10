import allure

from data.test_data import (
    ADDRESS_FROM,
    ADDRESS_FROM_KEY,
    ADDRESS_TO,
    ADDRESS_TO_KEY,
)
from pages.main_page import MainPage


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("На карте отображаются две точки маршрута")
    def test_two_points_are_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.build_route(ADDRESS_FROM, ADDRESS_TO)

        pins = main_page.route_pin_texts()
        pins_lower = [pin.lower() for pin in pins]

        assert main_page.route_pins_count() == 2
        assert any(ADDRESS_FROM_KEY in pin for pin in pins_lower)
        assert any(ADDRESS_TO_KEY in pin for pin in pins_lower)