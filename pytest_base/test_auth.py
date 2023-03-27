import pytest
import requests

url_login = "https://playground.learnqa.ru/api/user/login"
url_auth = "https://playground.learnqa.ru/api/user/auth"

class TestAuth:
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

        assert "auth_sid" in login_response.cookies, "There is auth cookie" #куки показывающие что мы авторизованы
        assert "x-csrf-token" in login_response.headers, "There is no CSRF token in auth headers" #заголовок отвечающий за безопасность
        assert "user_id" in login_response.json(), "There is no user id in login_response" #Логика ответа с бэка, которая проверяется

        self.auth_sid = login_response.cookies.get("auth_sid")
        self.token = login_response.headers.get("x-csrf-token")
        self.user_id_from_login = login_response.json()["user_id"]

    def test_positive_auth(self):
        auth_response = requests.get(url_auth,
                                     headers={
                                         "x-csrf-token":self.token,
                                     },
                                     cookies={"auth_sid":self.auth_sid})
        assert "user_id" in auth_response.json(), "There is no user id in auth_response"

        user_id_from_auth = auth_response.json()["user_id"]

        assert user_id_from_auth == self.user_id_from_login, f'' \
                                                        f'{self.user_id_from_auth} not equal' \
                                                        f'{self.user_id_from_login}'



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
        user_id_from_auth = auth_response.json()["user_id"]

        assert user_id_from_auth == 0, f'' \
                                       f'{user_id_from_auth} with condition: {condition}'