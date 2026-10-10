import allure

from data.test_data import (
    ADDRESS_FROM,
    ADDRESS_TO,
    DRIVE_BUTTON_TEXT,
    MODE_FAST,
    MODE_OPTIMAL,
    MODE_OWN,
    TAXI_BUTTON_TEXT,
)
from pages.main_page import MainPage
from pages.route_picker_page import RoutePickerPage


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:

    def _prepare_route(self, driver):
        main_page = MainPage(driver)
        main_page.build_route(ADDRESS_FROM, ADDRESS_TO)
        return RoutePickerPage(driver)

    @allure.title("При выборе 'Оптимальный' меняется активный таб")
    def test_optimal_mode_becomes_active(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_OPTIMAL)

        assert picker.active_mode() == MODE_OPTIMAL

    @allure.title("При выборе 'Быстрый' меняется активный таб")
    def test_fast_mode_becomes_active(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_FAST)

        assert picker.active_mode() == MODE_FAST

    @allure.title("При переключении табов пересчитывается стоимость и время")
    def test_switching_modes_recalculates_results(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_OPTIMAL)
        optimal_text = picker.result_text()
        optimal_duration = picker.result_duration()

        picker.select_mode(MODE_FAST)
        fast_text = picker.result_text()
        fast_duration = picker.result_duration()

        assert (optimal_text, optimal_duration) != (
            fast_text,
            fast_duration,
        )

    @allure.title("В режиме 'Свой' активны все 6 типов передвижения")
    def test_own_mode_shows_six_transport_types(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_OWN)

        assert picker.active_mode() == MODE_OWN
        assert picker.type_count() == 6
        assert picker.types_are_enabled()

    @allure.title("В режиме 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_fast_mode_has_taxi_button(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_FAST)

        assert picker.action_button_text() == TAXI_BUTTON_TEXT

    @allure.title("В режиме 'Свой' с типом 'Драйв' активна кнопка 'Забронировать'")
    def test_drive_mode_has_booking_button(self, driver):
        picker = self._prepare_route(driver)

        picker.select_mode(MODE_OWN)
        picker.select_drive()

        assert picker.action_button_text() == DRIVE_BUTTON_TEXT