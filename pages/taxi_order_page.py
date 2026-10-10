from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import TaxiOrderLocators


class TaxiOrderPage(BasePage):

    def tariff_names(self):
        cards = self.find_all_present(TaxiOrderLocators.TARIFF_CARDS)
        return [
            card.find_element(*TaxiOrderLocators.TARIFF_TITLE).text
            for card in cards
        ]

    def tariff_count(self):
        return len(self.find_all_present(TaxiOrderLocators.TARIFF_CARDS))

    def active_tariff_names(self):
        cards = self.find_all_present(TaxiOrderLocators.TARIFF_CARDS)
        return [
            card.find_element(*TaxiOrderLocators.TARIFF_TITLE).text
            for card in cards
            if "active"
            in (card.get_attribute("class") or "").split()
        ]

    def select_tariff(self, name):
        cards = self.find_all_present(TaxiOrderLocators.TARIFF_CARDS)
        for card in cards:
            title = card.find_element(
                *TaxiOrderLocators.TARIFF_TITLE
            ).text
            if title == name:
                card.click()
                return
        raise AssertionError(f"Тариф не найден: {name}")

    def show_tariff_tooltip(self, index):
        self.driver.execute_script(
            """
            document.querySelectorAll(
                '.tariff-cards .tcard .i-button'
            ).forEach(function(el) {
                el.dispatchEvent(new MouseEvent('mouseout', {
                    bubbles: true, cancelable: true, view: window
                }));
            });
            """
        )

        self.wait.until(
            lambda d: all(
                "show" not in (el.get_attribute("class") or "").split()
                for el in d.find_elements(
                    By.CSS_SELECTOR,
                    ".__react_component_tooltip",
                )
                if el.get_attribute("id")
            )
        )

        self.driver.execute_script(
            f"""
            const card = document.querySelectorAll(
                '.tariff-cards .tcard'
            )[{index}];
            const button = card.querySelector('.i-button');
            ['mouseover', 'mouseenter', 'mousemove'].forEach(
                function(name) {{
                    button.dispatchEvent(new MouseEvent(name, {{
                        bubbles: true, cancelable: true, view: window
                    }}));
                }}
            );
            """
        )

        self.wait.until(
            lambda d: "show"
            in (
                d.find_element(
                    By.CSS_SELECTOR, f"#tariff-card-{index}"
                ).get_attribute("class")
                or ""
            ).split()
        )

    def tooltip_title(self, index):
        tooltip = self.find_present(
            (By.CSS_SELECTOR, f"#tariff-card-{index}")
        )
        title_el = self.wait.until(
            lambda d: tooltip.find_element(
                *TaxiOrderLocators.TOOLTIP_TITLE
            )
        )
        self.wait.until(lambda d: title_el.text.strip() != "")
        return title_el.text.strip()

    def tooltip_description(self, index):
        tooltip = self.find_present(
            (By.CSS_SELECTOR, f"#tariff-card-{index}")
        )
        desc_el = self.wait.until(
            lambda d: tooltip.find_element(
                *TaxiOrderLocators.TOOLTIP_DESCRIPTION
            )
        )
        self.wait.until(lambda d: desc_el.text.strip() != "")
        return desc_el.text.strip()

    def form_fields_are_present(self):
        phone = self.find_visible(TaxiOrderLocators.PHONE_BUTTON)
        payment = self.find_visible(TaxiOrderLocators.PAYMENT_BUTTON)
        comment = self.find_visible(TaxiOrderLocators.COMMENT_INPUT)
        requirements = self.find_visible(
            TaxiOrderLocators.REQUIREMENTS_HEADER
        )
        return all((phone, payment, comment, requirements))

    def fill_comment(self, text):
        self.type_text(TaxiOrderLocators.COMMENT_INPUT, text)

    def open_requirements(self):
        self.click(TaxiOrderLocators.REQUIREMENTS_HEADER)

    def requirements_are_open(self):
        element = self.find_visible(TaxiOrderLocators.REQUIREMENTS_BLOCK)
        return "open" in (element.get_attribute("class") or "").split()

    def select_laptop_table_requirement(self):
        element = self.find_present(
            TaxiOrderLocators.LAPTOP_REQUIREMENT_SWITCH
        )
        self.driver.execute_script(
            "arguments[0].click();", element
        )

    def click_order(self):
        self.click(TaxiOrderLocators.ORDER_BUTTON)