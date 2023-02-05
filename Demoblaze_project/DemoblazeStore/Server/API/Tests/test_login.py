import pytest
from DemoblazeStore.Server.API.Locators.login_locators import LoginLocators
import allure
import requests

class Test_Login:
    @allure.description('Login correctly')
    @pytest.mark.Sanity
    def test_login_correctly(self):
        url = LoginLocators.url_login
        data = LoginLocators.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10


