import time
import allure
import pytest
from DemoblazeStore.Page.home_phone_page import PhonePage
from DemoblazeStore.base.base_test import BaseTest
class Test_Phone_Page(BaseTest):
    @allure.description("valid test")
    @pytest.mark.sanity
    def test_phones(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro good job", alt, "thank you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty name")
    @pytest.mark.sanity
    def test_phones_empty_name(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro good job", alt, "good job")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty country")
    @pytest.mark.sanity
    def test_phones_empty_country(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("werkineh")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty city")
    @pytest.mark.sanity
    def test_phones_empty_city(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty creadite card")
    @pytest.mark.sanity
    def test_phones_empty_creadite_card(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty month")
    @pytest.mark.sanity
    def test_phones_empty_month(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order("2023")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()

    @allure.description("empty month")
    @pytest.mark.sanity
    def test_phones_empty_month(self):
        self.driver = super().init()
        new_cart = PhonePage(self.driver)
        new_cart.click_home_text()
        new_cart.click_back_role_button_slide()
        new_cart.click_next_role_button_slide()
        new_cart.click_CATAGORIES_text()
        new_cart.click_phone_page()
        new_cart.click_samsung_galaxy_s6()
        new_cart.click_add_to_cart()
        time.sleep(4)
        alt = self.driver.switch_to.alert.text
        print("yeah bro nice to let us go ", alt, "I belive you")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        new_cart.click_cart_text()
        time.sleep(5)
        new_cart.click_place_order()
        time.sleep(5)
        new_cart.enter_name_of_place_order("werkinehfikadu@gmail.com")
        new_cart.enter_country_of_place_order("Ethiopia")
        new_cart.enter_city_of_place_order("Addis")
        new_cart.enter_creadite_card("5629866554864")
        new_cart.enter_month_of_place_order("april")
        new_cart.enter_year_of_place_order(" ")
        new_cart.click_purchase_place_order()
        new_cart.ok_you_purchase()
        time.sleep(3)
        new_cart.click_cloth_purchase()





















