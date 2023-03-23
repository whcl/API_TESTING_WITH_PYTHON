import requests

URL = 'https://playground.learnqa.ru/api/get_text'
r = requests.get(URL)
print(r.text)

