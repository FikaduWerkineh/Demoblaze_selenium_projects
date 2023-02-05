import time

import allure
import pytest
from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.log_in_page import LogInPage

class Test_LogIn_Page(BaseTest):
    @allure.description("valid user name and password")
    @pytest.mark.sanity
    def test_log_valid_user_name_and_password(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("werkinehfikadu@gmail.com")
        new_log_in.enter_password("fikadulove22")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(1)
        assert self.driver.title == "STORE"
        # xy = self.driver.switch_to.alert.text
        # assert xy == "Welcome werkinehfikadu@gmail.com"
        # self.driver.switch_to.alert.accept()

    @allure.description("")
    @pytest.mark.sanity
    def test_log_in_valid_user_name(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("asd@gmail.com")
        new_log_in.enter_password("fikadulove22")
        time.sleep(5)
        new_log_in.click_log_in_text()
        xy = self.driver.switch_to.alert.text
        assert xy == "User does not exist."
        self.driver.switch_to.alert.accept()

    @allure.description("empty user name")
    @pytest.mark.sanity
    def test_log_empty_user_name(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username(" ")
        new_log_in.enter_password("fikdulove22")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()


    @allure.description("empty password")
    @pytest.mark.sanity
    def test_log_empty_password(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("werkinehfikadu@gmail.com")
        new_log_in.enter_password(" ")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()

    @allure.description("special caracter username")
    @pytest.mark.sanity
    def test_log_special_caracter_user_name(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("@#$%^^&*()")
        new_log_in.enter_password("fikadulove22")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()

    @allure.description("special caracter password")
    @pytest.mark.sanity
    def test_log_special_caracter_password(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("werkinehfikadu@gmail.com")
        new_log_in.enter_password("~!@#$%^&*()")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()

    @allure.description("number username")
    @pytest.mark.sanity
    def test_log_special_number_user_name(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("12345")
        new_log_in.enter_password("fikadulove22")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()


    @allure.description("number password")
    @pytest.mark.sanity
    def test_log_special_number_password(self):
        self.driver = super().init()
        new_log_in = LogInPage(self.driver)
        new_log_in.click_log_in()
        new_log_in.enter_username("werkinehfikadu@gmail.com")
        new_log_in.enter_password("123456")
        time.sleep(5)
        new_log_in.click_log_in_text()
        time.sleep(5)
        xy = self.driver.switch_to.alert.text
        assert xy == "Wrong password."
        self.driver.switch_to.alert.accept()


