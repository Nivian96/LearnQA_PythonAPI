import requests

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.status_code, response.text)

response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "OPTIONS"})
print(response.status_code, response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response.status_code, response.text)

request_methods = [requests.get, requests.post, requests.put, requests.delete]
methods = ["GET", "POST", "PUT", "DELETE"]
for request_method in request_methods:
    for method in methods:
        if request_method.__name__ != "get":
            response = request_method("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
        else:
            response = request_method("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": method})

        if ((request_method.__name__ == method.lower()) and ("success" not in response.text)) or \
                ((request_method.__name__ != method.lower()) and ("success" in response.text)):
            print(request_method.__name__, method, response.text)
