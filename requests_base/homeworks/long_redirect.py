import requests

LONG_URL = "https://playground.learnqa.ru/api/long_redirect"

response = requests.get(LONG_URL)
for x in range(len(response.history)):
    print(f"current url - {x}:{response.history[x].url}")
print(f"last url is {x+1}: {response.url}")