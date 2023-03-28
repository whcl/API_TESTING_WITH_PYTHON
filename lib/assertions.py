from requests import Response
import json

class Assertions:

    @staticmethod #чтобы метод можно было вызывать без инициализации объекта
    def assert_json_value_by_name(response: Response, name, expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'

        assert name in response_as_dict, f"Response JSON has no key '{name}'"
        assert response_as_dict[name] == expected_value, error_massage

    @staticmethod
    def assert_json_value_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'

        assert name in response_as_dict, f"Response JSON has no key '{name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
       assert response.status_code == expected_status_code,f"Unexpected status code, expected: {expected_status_code}" \
                                                           f"Actual:{response.status_code}"


    def assert_json_value_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'

        assert name not in response_as_dict, f"Response JSON shouldn`t have key '{name}' " \
                                             f"but it`s present"

    @staticmethod
    def assert_json_value_has_keys(response: Response, names:list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'
        for name in names:
            assert name in response_as_dict, f"Response JSON has no key '{name}'"

    @staticmethod
    def assert_json_value_has_no_keys(response: Response, names:list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in json format. ' \
                          f'Response text is {response.text}'
        for name in names:
            assert name not in response_as_dict, f"Response JSON shouldn`t have key '{name}' " \
                                             f"but it`s present"