import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.test_data import (
    ADDRESS_FROM,
    ADDRESS_TO,
    BASE_URL,
    MODE_FAST,
)
from pages.main_page import MainPage
from pages.route_picker_page import RoutePickerPage
from pages.taxi_order_page import TaxiOrderPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def route_picker_page(driver):
    """Предусловие: маршрут построен, открыт блок выбора маршрута."""
    main_page = MainPage(driver)
    main_page.build_route(ADDRESS_FROM, ADDRESS_TO)
    return RoutePickerPage(driver)


@pytest.fixture
def taxi_order_page(driver):
    """Предусловие: открыта форма заказа такси (Быстрый режим)."""
    main_page = MainPage(driver)
    main_page.build_route(ADDRESS_FROM, ADDRESS_TO)
    picker = RoutePickerPage(driver)
    picker.select_mode(MODE_FAST)
    picker.click_action_button()
    return TaxiOrderPage(driver)