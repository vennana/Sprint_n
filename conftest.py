import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.test_data import BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()