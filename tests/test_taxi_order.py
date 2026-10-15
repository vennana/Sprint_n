import allure
import pytest

from data.test_data import (
    ADDRESS_FROM,
    ADDRESS_TO,
    ARRIVAL_SUBSTRING,
    COMMENT_TEXT,
    DETAILS_ADDRESS_FROM_LABEL,
    DETAILS_ADDRESS_TO_LABEL,
    DETAILS_PAYMENT_LABEL,
    DETAILS_TRIP_LABEL,
    ORDER_SEARCH_TITLE,
    TAXI_TARIFF_DESCRIPTIONS,
    TAXI_TARIFFS,
    TIMER_TIMEOUT_SECONDS,
    WORKING_TARIFF,
)
from pages.order_window_page import OrderWindowPage


@allure.feature("Заказ тарифа Такси")
class TestTaxiOrder:

    @allure.title("В форме заказа отображаются 6 тарифов по ТЗ")
    def test_six_taxi_tariffs_are_shown(self, taxi_order_page):
        taxi = taxi_order_page
        assert taxi.tariff_count() == 6
        assert taxi.tariff_names() == TAXI_TARIFFS

    @allure.title("Один из 6 тарифов активен по умолчанию")
    def test_one_tariff_is_active_by_default(self, taxi_order_page):
        taxi = taxi_order_page
        assert len(taxi.active_tariff_names()) == 1

    @allure.title("Тултип тарифа 'Рабочий' соответствует ТЗ")
    def test_working_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Рабочий")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Рабочий"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Рабочий"]
        )

    @pytest.mark.xfail(
        reason=(
            "Баг: описание тарифа 'Сонный' в UI — "
            "'Если мысли не выходят из головы', "
            "по ТЗ должно быть 'Для тех, кто не выспался'. "
            "Спутано с тарифом 'Разговорчивый'."
        )
    )
    @allure.title("Тултип тарифа 'Сонный' соответствует ТЗ")
    def test_sleepy_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Сонный")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Сонный"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Сонный"]
        )

    @pytest.mark.xfail(
        reason=(
            "Баг: описание тарифа 'Разговорчивый' в UI — "
            "'Для тех, кто не выспался', "
            "по ТЗ должно быть 'Если мысли не выходят из головы'. "
            "Спутано с тарифом 'Сонный'."
        )
    )
    @allure.title("Тултип тарифа 'Разговорчивый' соответствует ТЗ")
    def test_talkative_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Разговорчивый")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Разговорчивый"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Разговорчивый"]
        )

    @pytest.mark.xfail(
        reason=(
            "Баг: кнопка .i-button внутри карточки тарифа 'Отпускной' "
            "(второй ряд) имеет CSS-свойство display: none — "
            "React не монтирует элемент корректно, тултип не открывается. "
            "Тест не проходит по причине бага вёрстки, а не кода автотестов."
        )
    )
    @allure.title("Тултип тарифа 'Отпускной' соответствует ТЗ")
    def test_vacation_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Отпускной")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Отпускной"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Отпускной"]
        )

    @pytest.mark.xfail(
        reason=(
            "Баг: кнопка .i-button внутри карточки тарифа 'Утешительный' "
            "(второй ряд) имеет CSS-свойство display: none — "
            "React не монтирует элемент корректно, тултип не открывается. "
            "Тест не проходит по причине бага вёрстки, а не кода автотестов."
        )
    )
    @allure.title("Тултип тарифа 'Утешительный' соответствует ТЗ")
    def test_comforting_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Утешительный")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Утешительный"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Утешительный"]
        )

    @pytest.mark.xfail(
        reason=(
            "Баг: кнопка .i-button внутри карточки тарифа 'Глянцевый' "
            "(второй ряд) имеет CSS-свойство display: none — "
            "React не монтирует элемент корректно, тултип не открывается. "
            "Тест не проходит по причине бага вёрстки, а не кода автотестов."
        )
    )
    @allure.title("Тултип тарифа 'Глянцевый' соответствует ТЗ")
    def test_glossy_tariff_tooltip(self, taxi_order_page):
        taxi = taxi_order_page
        index = TAXI_TARIFFS.index("Глянцевый")
        taxi.show_tariff_tooltip(index)
        assert taxi.tooltip_title(index) == "Глянцевый"
        assert (
            taxi.tooltip_description(index)
            == TAXI_TARIFF_DESCRIPTIONS["Глянцевый"]
        )

    @allure.title(
        "Форма заказа содержит Телефон, Оплату, Комментарий, Требования"
    )
    def test_order_form_fields_are_present(self, taxi_order_page):
        taxi = taxi_order_page
        assert taxi.form_fields_are_present()

    @pytest.mark.slow
    @allure.title("После заказа открывается окно поиска машины")
    def test_order_search_window_is_shown(self, taxi_order_page):
        taxi = taxi_order_page
        taxi.select_tariff(WORKING_TARIFF)
        taxi.open_requirements()
        taxi.select_laptop_table_requirement()
        taxi.fill_comment(COMMENT_TEXT)
        taxi.click_order()

        order = OrderWindowPage(taxi.driver)
        assert order.is_shown()
        assert ORDER_SEARCH_TITLE in order.title()

    @pytest.mark.slow
    @allure.title(
        "После завершения поиска в деталях указаны адреса, оплата и стоимость"
    )
    def test_completed_order_details(self, taxi_order_page):
        taxi = taxi_order_page
        taxi.select_tariff(WORKING_TARIFF)
        taxi.open_requirements()
        taxi.select_laptop_table_requirement()
        taxi.fill_comment(COMMENT_TEXT)
        taxi.click_order()

        order = OrderWindowPage(taxi.driver)
        order.wait_for_completed_order(TIMER_TIMEOUT_SECONDS)
        assert ARRIVAL_SUBSTRING in order.title()

        order.click_button("Детали")
        order.wait_for_details()
        details = order.details_texts()

        assert details[DETAILS_ADDRESS_FROM_LABEL] == ADDRESS_FROM
        assert details[DETAILS_ADDRESS_TO_LABEL] == ADDRESS_TO
        assert DETAILS_PAYMENT_LABEL in details

        cost_row = [
            subheader
            for subheader, header in details.items()
            if header == DETAILS_TRIP_LABEL
        ]
        assert len(cost_row) == 1
        assert "Стоимость" in cost_row[0]
        assert "₽" in cost_row[0]