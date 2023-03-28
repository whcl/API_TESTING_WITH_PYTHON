import json

from requests import Response
from datetime import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'' \
                                                f'Cannot find cookie {cookie_name} in response'
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f'' \
                                                f'Cannot find header {header_name} in response'
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'

        assert name in response_as_dict, f"Response JSON has no key '{name}'"

        return response_as_dict[name]

    def get_auth_data(self, response: Response):
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_login = self.get_json_value(response, "user_id")
        return (auth_sid, token, user_id_from_login)

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = 'learnqa'
            domain = 'example.com'
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f'{base_part}{random_part}@{domain}'
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }