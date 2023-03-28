import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase

url_login = "https://playground.learnqa.ru/api/user/login"


class TestEditUser(BaseCase):
    def setup(self):

        #register
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_has_key(response, "id")

        self.email = data['email']
        self.first_name = data['firstName']
        self.last_name = data['lastName']
        self.password = data['password']
        self.user_id = self.get_json_value(response, "id")

        #login
        data ={
            'email':self.email,
            'password':self.password
        }
        login_response = requests.post(url_login, data=data)
        self.auth_sid, self.token, _ = self.get_auth_data(login_response)

    def test_edit_user(self):
        new_name = "Changed name"
        edit_response = requests.put(f"https://playground.learnqa.ru/api/user/{self.user_id}",
                                     headers={
                                         "x-csrf-token": self.token,
                                     },
                                     cookies={"auth_sid": self.auth_sid},
                                     data={
                                         'firstName': new_name
                                     })
        Assertions.assert_code_status(edit_response,200)

        #GET EDIT DATA
        get_response = requests.get(f"https://playground.learnqa.ru/api/user/{self.user_id}",
                                headers={
                                    "x-csrf-token": self.token,
                                },
                                cookies={"auth_sid": self.auth_sid})

        expected_fields = ["id", "username", "email", "firstName", "lastName"]
        Assertions.assert_code_status(get_response, 200)
        Assertions.assert_json_value_by_name(get_response, "firstName", new_name,
                                             "Wrong user name after edit")