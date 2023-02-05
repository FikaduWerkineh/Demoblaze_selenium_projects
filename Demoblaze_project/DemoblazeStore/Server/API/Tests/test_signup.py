

import pytest
from DemoblazeStore.Server.API.Locators.sign_up_locators import SignupLocators
import allure
import requests

class Test_Signup:
    @allure.description('Signup correctly')
    @pytest.mark.Sanity
    def test_signup_correctly(self):
        url =SignupLocators.url_Signup
        data = SignupLocators.data_valid
        res = requests.post(url, json=data)
        res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10



