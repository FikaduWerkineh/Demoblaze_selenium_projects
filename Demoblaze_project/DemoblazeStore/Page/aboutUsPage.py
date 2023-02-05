
from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.about_us_locators import AboutUsLocators

class Pages(AboutUsLocators):

    def __init__(self, driver):
        self.driver = driver

    def click_about_us_page(self):
        about_us = self.driver.find_element(By.XPATH, self.click_about_us_test_xpath)
        about_us.click()
    def click_on_vidio(self):
        video = self.driver.find_element(By.XPATH, self.select_vidio_test_xpath)
        video.click()
    def click_vidio_close(self):
        vidio_close = self.driver.find_element(By.XPATH, self.click_close_test_xpath)
        vidio_close.click()


