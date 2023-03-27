import requests
from utils import json_parser


URL = "https://playground.learnqa.ru/api/hello"
payload = {
    "name":"Vladimir"
}

r = requests.get(URL, params=payload)
parsed_json = json_parser(r)
print(parsed_json)


