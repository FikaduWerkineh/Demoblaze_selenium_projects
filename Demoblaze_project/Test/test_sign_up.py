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
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Sign up successful."
        self.driver.switch_to.alert.accept()





    allure.description("invalid user name")
    @pytest.mark.sanity
    def test_sign_up_empty_user_name_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("")
        new_sign_up.enter_password("")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        xy = self.driver.switch_to.alert.text
        assert xy == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()

    allure.description("invalid password")
    @pytest.mark.sanity
    def test_sign_up_invalid_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("fik")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()

    allure.description("number user name")
    @pytest.mark.sanity
    def test_sign_up_number_user_name(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("123456")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()


    allure.description("special caracter user name")
    @pytest.mark.sanity
    def test_sign_up_special_caracter_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("345678")
        new_sign_up.enter_password("fikadulove22")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "This user already exist."
        self.driver.switch_to.alert.accept()

    allure.description("number password")
    @pytest.mark.sanity
    def test_sign_up_number_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("123456")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()

    allure.description("special caracter password")
    @pytest.mark.sanity
    def test_sign_up_special_caracter_password(self):
        self.driver = super().init()
        new_sign_up = SignUpPage(self.driver)
        new_sign_up.click_sign_up_page()
        new_sign_up.enter_username("werkinehfikadu@gmail.com")
        new_sign_up.enter_password("!@#$%^")
        time.sleep(5)
        new_sign_up.click_sign_up_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "This user already exist."
        self.driver.switch_to.alert.accept()








