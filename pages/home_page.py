from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._cat_api_logo = (By.CSS_SELECTOR, "[alt='the cat api logo']")

    def is_logo_displayed(self):
        return self.driver.find_element(*self._cat_api_logo).is_displayed()
