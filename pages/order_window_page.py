from pages.base_page import BasePage
from pages.locators import OrderWindowLocators


class OrderWindowPage(BasePage):

    def is_shown(self):
        return self.wait_until_visible(
            OrderWindowLocators.ORDER_WINDOW
        ).is_displayed()

    def is_hidden(self):
        return self.wait_until_invisible(
            OrderWindowLocators.ORDER_WINDOW
        )

    def title(self):
        return self.find_visible(OrderWindowLocators.ORDER_TITLE).text

    def wait_for_completed_order(self, timeout):
        self.wait_for_condition(
            lambda d: "мин. и приедет"
            in d.find_element(*OrderWindowLocators.ORDER_TITLE).text,
            timeout=timeout,
        )

    def click_button(self, button_text):
        groups = self.find_all_present(
            OrderWindowLocators.BUTTON_GROUPS
        )
        for group in groups:
            if button_text in group.text:
                group.find_element(
                    *OrderWindowLocators.ORDER_BUTTON
                ).click()
                return
        raise AssertionError(f"Кнопка не найдена: {button_text}")

    def wait_for_details(self):
        self.wait_for_condition(
            lambda d: len(
                d.find_elements(*OrderWindowLocators.DETAILS_ROWS)
            ) > 0
        )

    def details_texts(self):
        rows = self.find_all_present(OrderWindowLocators.DETAILS_ROWS)
        result = {}
        for row in rows:
            header = row.find_element(
                *OrderWindowLocators.DETAILS_HEADER
            ).text.strip()
            subheader = row.find_element(
                *OrderWindowLocators.DETAILS_SUBHEADER
            ).text.strip()
            result[subheader] = header
        return result