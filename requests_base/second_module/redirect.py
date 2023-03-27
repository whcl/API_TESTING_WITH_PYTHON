import requests


""""
Проверка редиректа и его шагов
"""

URL = "https://playground.learnqa.ru/api/get_301/"


r = requests.get(URL, allow_redirects=False)
print(f"status {r.status_code}, url {r.url}")


r = requests.get(URL, allow_redirects=True)
first_url = r.history[0]
first_url_location = first_url.headers['location'] #прямой переход
print(f'location = {first_url_location}')
second_response = requests.get(first_url_location)
print(f"second url status {second_response.status_code}")
second_url = r.url
print(f"first url {first_url.url}, status {first_url.status_code}")
print(f"status {r.status_code}, url {r.url}")
