import time

import allure
import pytest

from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.sign_up_page import SignUpPage
class Test_Sign_Up_Page(BaseTest):
    @allure.description("valid user name and password")
    @pytest.mark.sanity
    def test_sign_up_valid(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("invalid user name")
    @pytest.mark.sanity
    def test_sign_up_invalid_user_name(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehasdfghj@gmail.com")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("invalid password")
    @pytest.mark.sanity
    def test_sign_up_invalid_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("12345678")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("number user name")
    @pytest.mark.sanity
    def test_sign_up_number_user_name(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("12345678")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("number password")
    @pytest.mark.sanity
    def test_sign_up_number_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("12345678")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("special cracter user name")
    @pytest.mark.sanity
    def test_sign_up_vspecial_caracter_user_name(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("@#$%^&$%^&*")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()

    allure.description("special_caracter_password")
    @pytest.mark.sanity
    def test_sign_up_valid(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("*&^%$#@")
        time.sleep(5)
        new_sign_up.click_sign_up_text()






