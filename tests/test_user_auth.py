import pytest
import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.logger_request import LoggerRequest

url_login = "/user/login"
url_auth = "/user/auth"


# TODO - Отредактирвать тесты с учетом новых проверок и методов в BaseCase

@allure.epic("Authorization cases")
class TestAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):  # настройка окружения
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        login_response = LoggerRequest.post(url_login, data=data)

        self.auth_sid = self.get_cookie(login_response, "auth_sid")
        self.token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_login = self.get_json_value(login_response, "user_id")

    @allure.description("This test successfully authorize user by email and password")
    def test_positive_auth(self):
        auth_response = LoggerRequest.get(url_auth,
                                          headers={
                                              "x-csrf-token": self.token,
                                          },
                                          cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            auth_response, "user_id", self.user_id_from_login, "User id from login is not equal to user id from auth"
        )

    @allure.description("This test checks authorization without cookie or token")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth(self, condition):
        if condition == "no_cookie":
            auth_response = LoggerRequest.get(url_auth,
                                              headers={
                                                  "x-csrf-token": self.token
                                              })
        elif condition == "no_token":
            auth_response = LoggerRequest.get(url_auth,
                                              cookies={
                                                  "auth_sid": self.auth_sid
                                              })

        Assertions.assert_json_value_by_name(
            auth_response, "user_id", 0, f"User id from login is not equal to 0 "
                                         f"with condition {condition}")
