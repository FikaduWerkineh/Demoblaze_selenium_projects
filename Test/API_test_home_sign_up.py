from Locatores.locatores import *
import allure
import requests
import pytest


class Test_valid:
    @allure.description("test_valid")
    @pytest.mark.sanity
    def test_web_correctly(self):
        url = Locatores.url
        data = Locatores.correct_body
        response = requests.post(url, json=data)
        response_data = response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10