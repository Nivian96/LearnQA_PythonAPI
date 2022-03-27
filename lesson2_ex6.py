import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
redirects_count = len(response.history)
last_response = response
print(redirects_count, last_response.url)
