from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import RoutePickerLocators


class RoutePickerPage(BasePage):
    def is_shown(self):
        return self.find_visible(RoutePickerLocators.TYPE_PICKER).is_displayed()

    def mode_names(self):
        modes = self.find_all_visible(RoutePickerLocators.MODES)
        return [mode.text for mode in modes]

    def select_mode(self, name):
        locator = (
            By.XPATH,
            "//div[contains(@class,'modes-container')]"
            f"//div[contains(@class,'mode') "
            f"and normalize-space()='{name}']",
        )
        self.click(locator)

    def active_mode(self):
        return self.find_visible(RoutePickerLocators.ACTIVE_MODE).text

    def type_count(self):
        return len(self.find_all_present(RoutePickerLocators.TYPES))

    def types_are_enabled(self):
        elements = self.find_all_present(RoutePickerLocators.TYPES)
        return all(
            "disabled" not in (el.get_attribute("class") or "")
            for el in elements
        )

    def select_drive(self):
        self.click(RoutePickerLocators.DRIVE_TYPE)

    def active_type_class(self):
        element = self.find_visible(RoutePickerLocators.ACTIVE_TYPE)
        return element.get_attribute("class") or ""

    def result_text(self):
        return self.find_visible(RoutePickerLocators.RESULT_TEXT).text

    def result_duration(self):
        return self.find_visible(RoutePickerLocators.RESULT_DURATION).text

    def action_button_text(self):
        return self.find_visible(RoutePickerLocators.RESULT_BUTTON).text

    def click_action_button(self):
        self.click(RoutePickerLocators.RESULT_BUTTON)

    def result_blocks_text(self):
        elements = self.find_all_present(RoutePickerLocators.RESULTS)
        return [element.text for element in elements]