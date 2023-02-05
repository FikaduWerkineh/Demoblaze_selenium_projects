import time

from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.home_phone_locators import PhoneLocators
class PhonePage(PhoneLocators):
    def __init__(self, driver):
        self.driver = driver
    def click_home_text(self):
        homes = self.driver.find_element(By.XPATH, self.click_home_text_xpath)
        homes.click()
    def click_back_role_button_slide(self):
        back_roles = self.driver.find_element(By.XPATH, self.click_back_role_button_slide_xpath)
        back_roles.click()
    def click_next_role_button_slide(self):
        next_role = self.driver.find_element(By.XPATH, self.click_next_role_button_slide_xpath)
        next_role.click()
    def click_CATAGORIES_text(self):
        CATAGORIES= self.driver.find_element(By.XPATH, self.click_CATAGORIES_text_xpath)
        CATAGORIES.click()
    def click_phone_page(self):
        phones = self.driver.find_element(By.XPATH, self.click_phone_page_xpath)
        phones.click()
    def click_samsung_galaxy_s6(self):
        samsung_galaxies_s6 = self.driver.find_element(By.XPATH, self.click_samsung_galaxy_s6_xpath)
        samsung_galaxies_s6.click()
    def click_add_to_cart(self):
        add_to_carts = self.driver.find_element(By.XPATH, self.click_add_to_cart_xpath)
        add_to_carts.click()
    def click_cart_text(self):
        carts = self.driver.find_element(By.XPATH, self.click_cart_text_xpath)
        carts.click()
        time.sleep(5)
    def click_place_order(self):
        place_orders = self.driver.find_element(By.XPATH, self.click_place_order_xpath)
        place_orders.click()
    def enter_name_of_place_order(self, name):
        names = self.driver.find_element(By.ID, self.enter_Name_of_place_order_id)
        names.send_keys(name)

    def enter_country_of_place_order(self, country):
        countries = self.driver.find_element(By.ID, self.enter_country_of_place_order_id)
        countries.send_keys(country)

    def enter_city_of_place_order(self, city):
        cities = self.driver.find_element(By.ID, self.place_order_city_id)
        cities.send_keys(city)

    def enter_creadite_card(self, creadite_card):
        creadites = self.driver.find_element(By.ID, self.enter_creadite_card_id)
        creadites.send_keys(creadite_card)

    def enter_month_of_place_order(self, month):
        months = self.driver.find_element(By.ID, self.enter_place_month_id)
        months.send_keys(month)

    def enter_year_of_place_order(self, year):
        years = self.driver.find_element(By.ID, self.enter_place_order_year_id)
        years.send_keys(year)

    def click_purchase_place_order(self):
        pur = self.driver.find_element(By.XPATH, self.click_purchase_place_order_xpath)
        pur.click()
    def ok_you_purchase(self):
        self.driver.find_element(By.XPATH, self.ok_you_purchase_xpath)

    def click_cloth_purchase(self):
        purchases = self.driver.find_element(By.XPATH, self.click_cloth_purchase_xpath)
        purchases.click()









