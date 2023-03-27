import requests

URL = "https://playground.learnqa.ru/api/get_auth_cookie"

payload = {
    "login":"secret_login",
    "password":"secret_pass"
}

response = requests.post(url=URL, data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies)) #превращаем в словарь и удобно используем
#print(response.headers)


URL_CHECK = "https://playground.learnqa.ru/api/check_auth_cookie"

cookie_value = response.cookies.get('auth_cookie') # можно если писать универсально, то по ключам словаря пройитись.
cookies = {
    'auth_cookie':cookie_value
}
auth_response = requests.post(URL_CHECK, cookies=cookies)

print(f"auth resposne is {auth_response.text}")