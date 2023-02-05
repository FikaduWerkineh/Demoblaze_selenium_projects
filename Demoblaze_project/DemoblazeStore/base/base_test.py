import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    driver = webdriver.Chrome()
    @pytest.mark.sanity
    @allure.description("first test")
    def init(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        return self.driver

    def teardown(self):
        # self.driver.close()
        self.driver.quit()
