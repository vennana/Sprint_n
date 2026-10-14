from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all_present(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_text_in_element(self, locator, substring, timeout=None):
        wait = WebDriverWait(
            self.driver, timeout if timeout else self.TIMEOUT
        )
        return wait.until(
            lambda d: substring in d.find_element(*locator).text
        )

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def wait_for_condition(self, condition, timeout=None):
        wait = WebDriverWait(
            self.driver, timeout if timeout else self.TIMEOUT
        )
        return wait.until(condition)

    def get_element_attribute(self, locator, attribute):
        return self.find_present(locator).get_attribute(attribute)

    def find_elements_by_selector(self, css_selector):
        return self.driver.find_elements("css selector", css_selector)