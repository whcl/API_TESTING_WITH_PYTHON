import pytest
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions

url_login = "https://playground.learnqa.ru/api/user/login"
url_auth = "https://playground.learnqa.ru/api/user/auth"

class TestAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self): #настройка окружения
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        login_response = requests.post(url_login, data=data)

        self.auth_sid = self.get_cookie(login_response, "auth_sid")
        self.token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_login = self.get_json_value(login_response, "user_id")


    def test_positive_auth(self):
        auth_response = requests.get(url_auth,
                                     headers={
                                         "x-csrf-token":self.token,
                                     },
                                     cookies={"auth_sid":self.auth_sid})

        Assertions.assert_json_value_by_name(
            auth_response, "user_id", self.user_id_from_login,"User id from login is not equal to user id from auth"
        )


    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth(self, condition):
        if condition == "no_cookie":
            auth_response = requests.get(url_auth,
                                         headers={
                                             "x-csrf-token":self.token
                                         })
        elif condition == "no_token":
            auth_response = requests.get(url_auth,
                                         cookies={
                                             "auth_sid":self.auth_sid
                                         })

        Assertions.assert_json_value_by_name(
            auth_response, "user_id", 0, f"User id from login is not equal to 0 "
                                         f"with condition {condition}")