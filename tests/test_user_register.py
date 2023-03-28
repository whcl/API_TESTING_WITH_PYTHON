from datetime import datetime

from lib.logger_request import LoggerRequest
from lib.base_case import BaseCase
from lib.assertions import Assertions


# TODO - Отредактирвать тесты с учетом новых проверок и методов в BaseCase

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f'{base_part}{random_part}@{domain}'

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = LoggerRequest.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"" \
                                                   f"Users with email '{email}' " \
                                                   f"already exists Unexpected content {response.content} "

    def test_success_create_user(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = LoggerRequest.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_has_key(response, "id")