import time

import allure
import pytest

from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.contact_us_page import ContactUsPage
class Test_Contact_Us_Page(BaseTest):
    @allure.description("valid test")
    @pytest.mark.sanity
    def test_contacts_us_valid_email(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("werkinehfikadu@gmail.com")
        new_contact.enter_contact_name("werkineh")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

    @allure.description("valid email and password")
    @pytest.mark.sanity
    def test_contacts_us_valid_email_password(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("werkinehfikadu@gmail.com")
        new_contact.enter_contact_name("fikadu")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

    @allure.description("empty name")
    @pytest.mark.sanity
    def test_contacts_us_empty_name(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("werkinehfikadu@gmail.com")
        new_contact.enter_contact_name(" ")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()



    @allure.description("number email")
    @pytest.mark.sanity
    def test_contacts_us_number_email(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("123456")
        new_contact.enter_contact_name("werkineh")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

    @allure.description(" empty email and  name")
    @pytest.mark.sanity
    def test_contacts_us_empty_email_and_name(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email(" ")
        new_contact.enter_contact_name(" ")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

    @allure.description("special caracter email")
    @pytest.mark.sanity
    def test_contacts_us_special_caracter_email_password(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email(" !@#$%^")
        new_contact.enter_contact_name("#$%^&")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

    @allure.description("special caracter password")
    @pytest.mark.sanity
    def test_contacts_us_special_caracter_password(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("werkinehfikadu@gmail.com")
        new_contact.enter_contact_name(" *&^%$#")
        time.sleep(2)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()
        xy = self.driver.switch_to.alert.text
        assert xy == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()

