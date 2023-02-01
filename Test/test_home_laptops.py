import time
import allure
import pytest
from DemoblazeStore.Page.home_laptops_page import LaptopsPage
from DemoblazeStore.base.base_test import BaseTest
class Test_Laptops_Page(BaseTest):
    @allure.description("valid test")
    @pytest.mark.sanity
    def test_laptops_page(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
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
       new_cart.ok_purchase()

    @allure.description("capital_letter_name")
    @pytest.mark.sanity
    def test_laptops_page_capital_letter_name(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("WERKINEH")
       new_cart.enter_country_of_place_order("Ethiopia")
       new_cart.enter_city_of_place_order("Addis")
       new_cart.enter_credite_card_of_place_order("5629866554864")
       new_cart.enter_month_of_place_order("april")
       new_cart.enter_year_of_place_order("2023")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()

    @allure.description("capiatal letter country")
    @pytest.mark.sanity
    def test_laptops_page_captal_letter_country(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("werkineh")
       new_cart.enter_country_of_place_order("ETHIOPIA")
       new_cart.enter_city_of_place_order("Addis")
       new_cart.enter_credite_card_of_place_order("5629866554864")
       new_cart.enter_month_of_place_order("april")
       new_cart.enter_year_of_place_order("2023")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()

    @allure.description("capital letter_city")
    @pytest.mark.sanity
    def test_laptops_page_capital_city(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("werkineh")
       new_cart.enter_country_of_place_order("Ethiopia")
       new_cart.enter_city_of_place_order("APRIL")
       new_cart.enter_credite_card_of_place_order("5629866554864")
       new_cart.enter_month_of_place_order("april")
       new_cart.enter_year_of_place_order("2023")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()

    @allure.description("spetial caracter")
    @pytest.mark.sanity
    def test_laptops_page_spetial_caracter(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("werkineh")
       new_cart.enter_country_of_place_order("Ethiopia")
       new_cart.enter_city_of_place_order("Addis")
       new_cart.enter_credite_card_of_place_order("58asdfg64")
       new_cart.enter_month_of_place_order("april")
       new_cart.enter_year_of_place_order("2023")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()

    @allure.description("capital letter month")
    @pytest.mark.sanity
    def test_laptops_page_capital_letter_month(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("werkineh")
       new_cart.enter_country_of_place_order("Ethiopia")
       new_cart.enter_city_of_place_order("Addis")
       new_cart.enter_credite_card_of_place_order("5629866554864")
       new_cart.enter_month_of_place_order("APRIL")
       new_cart.enter_year_of_place_order("2023")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()

    allure.description("special caoital letter year")
    @pytest.mark.sanity
    def test_laptops_page_capital_letter_year(self):
       self.driver = super().init()
       new_cart = LaptopsPage(self.driver)
       new_cart.click_home_text()
       new_cart.click_back_role_button_slide()
       new_cart.click_next_role_button_slide()
       new_cart.click_CATAGORIES_text()
       new_cart.click_laptops_page()
       new_cart.click_laptops_sony_vaio_i5()
       new_cart.click_add_to_cart()
       time.sleep(4)
       alt = self.driver.switch_to.alert.text
       print("yaap bro nice let us go ", alt, "I thank you")
       assert alt == "Product added"
       self.driver.switch_to.alert.accept()
       new_cart.click_cart_text()
       new_cart.click_place_order()
       new_cart.enter_name_of_place_order("werkineh")
       new_cart.enter_country_of_place_order("Ethiopia")
       new_cart.enter_city_of_place_order("Addis")
       new_cart.enter_credite_card_of_place_order("5629866554864")
       new_cart.enter_month_of_place_order("APRIL")
       new_cart.enter_year_of_place_order("20sdf23")
       new_cart.click_purchase_place_order()
       new_cart.ok_purchase()
