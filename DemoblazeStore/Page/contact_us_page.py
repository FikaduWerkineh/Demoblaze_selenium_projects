
from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.contact_us_locators import ContactUsLocators

class ContactUsPage(ContactUsLocators):
    def __init__(self, driver):
        self.driver = driver
    def click_contact_us_test(self):
        contacts = self.driver.find_element(By.XPATH, self.click_contact_us_test_xpath)
        contacts.click()
    def enter_contact_email(self, contact_email):
        contact_emails = self.driver.find_element(By.ID, self.enter_contactEmail_id)
        contact_emails.send_keys(contact_email)
    def enter_contact_name(self, contact_name):
        contactNames = self.driver.find_element(By.ID, self.enter_contactName_id)
        contactNames.send_keys(contact_name)
    def enter_message(self, message):
        messages = self.driver.find_element(By.ID, self.enter_message_id)
        messages.send_keys(message)
    def click_send_message_button(self):
         send_messages = self.driver.find_element(By.XPATH, self.click_send_message_button_xpath)
         send_messages.click()



