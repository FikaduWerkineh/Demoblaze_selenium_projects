
from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.home_monitors_locators import MonitorLocators
class Monitors_Page(MonitorLocators):
    def __init__(self, drive):
        self.driver = drive
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
    def click_monitors_text(self):
        mon = self.driver.find_element(By.XPATH, self.click_monitors_text_xpath)
        mon.click()
    def click_Apple_monitors_24(self):
        Apple_mon = self.driver.find_element(By.XPATH, self.click_Apple_monitors_24_xpath)
        Apple_mon.click()
    def click_add_to_cart(self):
        add_to_carts = self.driver.find_element(By.XPATH, self.click_add_to_cart_xpath)
        add_to_carts.click()
    def click_cart_text(self):
        carts = self.driver.find_element(By.XPATH, self.click_cart_text_xpath)
        carts.click()
    def click_place_order(self):
        place_orders = self.driver.find_element(By.XPATH, self.click_place_order_xpath)
        place_orders.click()

    def enter_name_of_place_order(self, name):
        names = self.driver.find_element(By.ID, self.enter_name_of_place_order_id)
        names.send_keys(name)

    def enter_country_of_place_order(self, country):
        countries = self.driver.find_element(By.ID, self.enter_country_of_place_order_id)
        countries.send_keys(country)

    def enter_city_of_place_order(self, city):
        cities = self.driver.find_element(By.ID, self.enter_place_order_city_id)
        cities.send_keys(city)

    def enter_credite_card_of_place_order(self, crdits):
        credit = self.driver.find_element(By.ID, self.enter_credit_card_id)
        credit.send_keys(crdits)

    def enter_month_of_place_order(self, mon):
        month = self.driver.find_element(By.ID, self.enter_place_month_id)
        month.send_keys(mon)

    def enter_year_of_place_order(self, ye):
        years = self.driver.find_element(By.ID, self.enter_place_order_year_id)
        years.send_keys(ye)

    def click_purchase_place_order(self):
        pur = self.driver.find_element(By.XPATH, self.click_purchase_place_order_xpath)
        pur.click()
    def ok_you_purchase(self):
        purchases = self.driver.find_element(By.XPATH, self.click_ok_you_purchase_xpath)
    def click_cloth_purchase(self):
        purchases = self.driver.find_element(By.XPATH, self.click_cloth_purchase_xpath)
        purchases.click()









    # def click_next_text(self):
    #     nexts = self.driver.find_element(By.XPATH, self.click_next_text_xpath)
    #     nexts.click()
    # def click_previous_text(self):
    #     prev = self.driver.find_element(By.XPATH, self.click_previous_text_xpath)
    #     prev.click()









