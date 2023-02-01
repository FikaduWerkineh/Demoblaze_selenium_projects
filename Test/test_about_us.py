
import allure
import pytest
from DemoblazeStore.base.base_test import BaseTest
from DemoblazeStore.Page.aboutUsPage import Pages
class Test_All_Pages(BaseTest):
    @allure.description("this is first test")
    @pytest.mark.sanity
    def test_about_us(self):
        self.driver = super().init()
        new = Pages(self.driver)
        new.click_about_us_page()
        new.click_on_vidio()
        new.click_vidio_close()



