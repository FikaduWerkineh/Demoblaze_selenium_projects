import allure
import pytest
import time

from DemoblazeStore.Page.home_monitors_page import Monitors_Page
from DemoblazeStore.base.base_test import BaseTest
class Test_Monitors_Page(BaseTest):
    @allure.description("valid test")
    @pytest.mark.sanity
    def test_monitors_page(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("number name")
    @pytest.mark.sanity
    def test_monitors_page_number_name(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("234567")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("number country")
    @pytest.mark.sanity
    def test_monitors_page_number_country(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order(" 12345")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("number city")
    @pytest.mark.sanity
    def test_monitors_page_number_city(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order(" 2345")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("name creadite card")
    @pytest.mark.sanity
    def test_monitors_page_name_creadite_card(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("asdfgh")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("number month")
    @pytest.mark.sanity
    def test_monitors_page_number_month(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("5432")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()

    @allure.description("name year")
    @pytest.mark.sanity
    def test_monitors_page_name_year(self):
        self.driver = super().init()
        new_cart = Monitors_Page(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_monitors_text()
        new_cart.click_Apple_monitors_24()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        new_cart.click_cart_text()
        new_cart.click_place_order()
        new_cart.enter_name_of_place_order("werkineh")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_credite_card_of_place_order("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("zxcvbn")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        new_cart.click_cloth_purchase()















