from selenium.webdriver.common.by import By


class MainLocators:
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    ROUTE_PINS = (By.CSS_SELECTOR, ".ymaps-2-1-79-route-pin__text")


class RoutePickerLocators:
    TYPE_PICKER = (By.CSS_SELECTOR, ".type-picker.shown")
    MODES = (By.CSS_SELECTOR, ".modes-container .mode")
    ACTIVE_MODE = (By.CSS_SELECTOR, ".modes-container .mode.active")
    TYPES = (By.CSS_SELECTOR, ".types-container .type")
    ACTIVE_TYPE = (By.CSS_SELECTOR, ".types-container .type.active")
    DRIVE_TYPE = (By.CSS_SELECTOR, ".types-container .type.drive")
    RESULT_TEXT = (By.CSS_SELECTOR, ".results-text .text")
    RESULT_DURATION = (By.CSS_SELECTOR, ".results-text .duration")
    RESULT_BUTTON = (By.CSS_SELECTOR, ".results-text .button.round")
    RESULTS = (By.CSS_SELECTOR, ".results-container")

    @staticmethod
    def mode_by_name(name):
        return (
            By.XPATH,
            "//div[contains(@class,'modes-container')]"
            f"//div[contains(@class,'mode') "
            f"and normalize-space()='{name}']",
        )


class TaxiOrderLocators:
    TARIFF_CARDS = (By.CSS_SELECTOR, ".tariff-cards .tcard")
    TARIFF_TITLE = (By.CSS_SELECTOR, ".tcard-title")
    TARIFF_PRICE = (By.CSS_SELECTOR, ".tcard-price")
    TARIFF_INFO_BUTTON = (By.CSS_SELECTOR, ".tcard .i-button")

    ALL_TOOLTIPS = (By.CSS_SELECTOR, ".__react_component_tooltip")
    ALL_TARIFF_BUTTONS = (
        By.CSS_SELECTOR, ".tariff-cards .tcard .i-button"
    )

    TOOLTIP = (By.CSS_SELECTOR, ".__react_component_tooltip.show")
    TOOLTIP_TITLE = (By.CSS_SELECTOR, ".i-floating .i-title")
    TOOLTIP_DESCRIPTION = (By.CSS_SELECTOR, ".i-floating .i-dPrefix")

    PHONE_BUTTON = (By.CSS_SELECTOR, ".form .np-button")
    PAYMENT_BUTTON = (By.CSS_SELECTOR, ".form .pp-button")
    COMMENT_INPUT = (By.ID, "comment")
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".reqs-header")
    REQUIREMENTS_BLOCK = (By.CSS_SELECTOR, ".reqs")
    LAPTOP_REQUIREMENT_SWITCH = (
        By.CSS_SELECTOR, ".r-type-switch .switch"
    )
    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    @staticmethod
    def tooltip_by_index(index):
        return (By.CSS_SELECTOR, f"#tariff-card-{index}")

    @staticmethod
    def tariff_button_by_index(index):
        return (
            By.CSS_SELECTOR,
            f".tariff-cards .tcard:nth-child({index + 1}) .i-button",
        )


class OrderWindowLocators:
    ORDER_WINDOW = (By.CSS_SELECTOR, ".order.shown")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    ORDER_TIME = (By.CSS_SELECTOR, ".order-header-time")
    BUTTON_GROUPS = (By.CSS_SELECTOR, ".order-btn-group")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".order-button")
    DETAILS_ROWS = (By.CSS_SELECTOR, ".order-details-row")
    DETAILS_HEADER = (By.CSS_SELECTOR, ".o-d-h")
    DETAILS_SUBHEADER = (By.CSS_SELECTOR, ".o-d-sh")