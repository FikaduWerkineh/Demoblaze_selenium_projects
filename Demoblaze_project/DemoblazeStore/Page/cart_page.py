from selenium.webdriver.common.by import By
from DemoblazeStore.Locators.cart_locators import CartLocators


class CartPage(CartLocators):
    def __init__(self, driver):
        self.driver = driver

    def click_cart_locators_text(self):
        cart = self.driver.find_element(By.ID, self.click_cart_locator_text_Id)
        cart.click()

    def click_place_order_button(self):
        place_order = self.driver.find_element(By.XPATH, self.click_place_order_button_xpath)
        place_order.click()

    def enter_name_of_place_order(self, name):
        names = self.driver.find_element(By.ID, self.enter_name_of_place_order_id)
        names.send_keys(name)

    def enter_country_of_place_order(self, country):
        countries = self.driver.find_element(By.ID, self.enter_country_of_place_order_id)
        countries.send_keys(country)

    def enter_city_of_place_order(self, city):
        cities = self.driver.find_element(By.ID, self.enter_place_order_city_id)
        cities.send_keys(city)

    def enter_credit_card_of_place_order(self, crdits):
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

    def textGetter(self):
        return self.driver.find_element(By.XPATH, self.thank_you_text).text
