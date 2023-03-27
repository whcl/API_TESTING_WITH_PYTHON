import json

from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies,f'' \
                                               f'Cannot find cookie {cookie_name} in response'
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers,f'' \
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