import requests
from utils import  set_auth_cookies

""""
Авторизация и получение куки
"""

URL_FOR_COOKIE = "https://playground.learnqa.ru/api/get_auth_cookie"
URL_WITH_AUTH = "https://playground.learnqa.ru/api/check_auth_cookie"

payload = {
    "login":"secret_login",
    "password":"secret_pass"
}

payload_wrong = {
    "login":"secret_login",
    "password":"secret_pass2"
}

response = requests.post(URL_FOR_COOKIE, data=payload)
response_with_auth = requests.post(URL_WITH_AUTH, cookies=set_auth_cookies(response))
print(f" good auth: {response_with_auth.text}")

response = requests.post(URL_FOR_COOKIE, data=payload_wrong)
response_with_auth = requests.post(URL_WITH_AUTH, cookies=set_auth_cookies(response))
print(f" wrong auth: {response_with_auth.text}")