from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.log_in_locators import LogInLocators
class LogInPage(LogInLocators):
    def __init__(self, driver):
        self.driver = driver

    def click_log_in(self):
        logIn = self.driver.find_element(By.ID, self.click_log_in_id)
        logIn.click()
    def enter_username(self, username):
        usernames = self.driver.find_element(By.ID, self.enter_username_id)
        usernames.send_keys(username)
    def enter_password(self, password):
        passwords = self.driver.find_element(By.ID, self.enter_password_id)
        passwords.send_keys(password)
    def click_log_in_text(self):
        log = self.driver.find_element(By.XPATH, self.click_log_in_text_xpath)
        log.click()
