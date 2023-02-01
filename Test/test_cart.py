import allure
import pytest
from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.cart_page import CartPage
class Test_Cart_Page(BaseTest):
    @allure.description("this is first test")
    @pytest.mark.sanity
    def test_carts_valid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    def test_carts_empty_name(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order(" ")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this second test")
    @pytest.mark.sanity
    def test_carts_empty_country(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()


    def test_carts_empty_city(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    def test_carts_empty_creadit_card(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    def test_carts_empty_month(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

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
        new_cart.enter_year_of_place_order("")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("wertyuiop")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Israel")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Israel")
        new_cart.enter_city_of_place_order("Beersheba")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Israel")
        new_cart.enter_city_of_place_order("Beersheba")
        new_cart.enter_credit_card_of_place_order("asdfghjkl")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Israel")
        new_cart.enter_city_of_place_order("Beersheba")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("jan")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()

    @allure.description("this 3rd test")
    @pytest.mark.sanity
    def test_carts_invalid(self):
        self.driver = super().init()
        new_cart = CartPage(self.driver)
        new_cart.click_cart_locators_text()
        new_cart.click_place_order_button()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Israel")
        new_cart.enter_city_of_place_order("Beersheba")
        new_cart.enter_credit_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2000")
        new_cart.click_purchase_place_order()

