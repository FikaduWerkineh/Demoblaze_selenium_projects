import time

import allure
import pytest
from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.cart_page import CartPage
class Test_Cart_Page(BaseTest):
    @allure.description("valid user name and password")
    @pytest.mark.sanity
    def test_carts_valid_user_name_and_password(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com ")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("123456")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"

    def test_carts_empty_name(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = self.driver.switch_to.alert.text
        assert xy == "Please fill out Name and Creditcard."
        self.driver.switch_to.alert.accept()

    @allure.description("valid country")
    @pytest.mark.sanity
    def test_carts_empty_country(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order(" ")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"

    def test_carts_empty_city(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order(" ")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"

    def test_carts_empty_creadit_card(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order(" ")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"

    def test_carts_empty_valid_month(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order(" ")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"

    def test_carts_empty_year(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order(" ")
        new_cart.click_purchase_place_order()
        xy = new_cart.textGetter()
        assert xy == "Thank you for your purchase!"



