import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions

url = "https://playground.learnqa.ru/api/user/"
url_login = "https://playground.learnqa.ru/api/user/login"

class TestUserGet(BaseCase):
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        login_response = requests.post(url_login, data=data)
        self.auth_sid = self.get_cookie(login_response, "auth_sid")
        self.token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_login = self.get_json_value(login_response, "user_id")

    def test_get_user_with_auth(self):
        response = requests.get(f"{url}/{self.user_id_from_login}",
                                headers={
                                    "x-csrf-token": self.token,
                                },
                                cookies={"auth_sid": self.auth_sid})

        expected_fields = ["id", "username", "email", "firstName", "lastName"]
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_has_keys(response, names=expected_fields)

    def test_get_user_with_no_auth(self):
        response = requests.get(f"{url}/{self.user_id_from_login}")

        Assertions.assert_code_status(response, 200)
        unexpected_fields = ["id", "email", "firstName", "lastName"]
        Assertions.assert_json_value_has_key(response, "username")
        Assertions.assert_json_value_has_no_keys(response, names=unexpected_fields)