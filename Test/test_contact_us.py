import time

import allure
import pytest

from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.contact_us_page import ContactUsPage
class Test_Contact_Us_Page(BaseTest):
    @allure.description("this is the first test")
    @pytest.mark.sanity
    def test_contacts_us_valid(self):
        self.driver = super().init()
        new_contact = ContactUsPage(self.driver)
        new_contact.click_contact_us_test()
        new_contact.enter_contact_email("werkinehfikadu@gmail.com")
        new_contact.enter_contact_name("werkineh")
        time.sleep(6)
        new_contact.enter_message("Hello")
        new_contact.click_send_message_button()

