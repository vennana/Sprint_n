from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import MainLocators


class MainPage(BasePage):

    def set_from(self, address):
        self._fill_address(MainLocators.FROM_INPUT, address)

    def set_to(self, address):
        self._fill_address(MainLocators.TO_INPUT, address)

    def build_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def route_pin_texts(self):
        pins = self.find_all_present(MainLocators.ROUTE_PINS)
        return [pin.text for pin in pins]

    def route_pins_count(self):
        return len(self.find_all_present(MainLocators.ROUTE_PINS))

    def _fill_address(self, locator, address):
        element = self.find_visible(locator)
        self.execute_script("arguments[0].click();", element)
        element.clear()
        element.send_keys(address)
        element.send_keys(Keys.ENTER)