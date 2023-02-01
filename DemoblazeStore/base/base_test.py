import allure
import pytest
from selenium import webdriver

@pytest.mark.sanity
@allure.description("first test")

class BaseTest:
    driver = webdriver.Chrome()

    def init(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        return self.driver

    def teardown(self):
        # self.driver.close()
        self.driver.quit()
