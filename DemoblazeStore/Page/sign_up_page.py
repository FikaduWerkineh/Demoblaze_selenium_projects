from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.sign_up_locators import SignUpLocators
class SignUpPage(SignUpLocators):
    def __init__(self, driver):
        self.driver = driver
    def click_sign_up_page(self):
        sign_ups = self.driver.find_element(By.XPATH, self.click_sign_up_page_xpath)
        sign_ups.click()
    def enter_username(self, username):
        usernames = self.driver.find_element(By.XPATH, self.enter_username_xpath)
        usernames.send_keys(username)
    def enter_password(self, password):
        passwords = self.driver.find_element(By.XPATH, self.enter_password_xpath)
        passwords.send_keys(password)
    def click_sign_up_text(self):
        signUps = self.driver.find_element(By.XPATH, self.click_sign_up_text_xpath)
        signUps.click()
