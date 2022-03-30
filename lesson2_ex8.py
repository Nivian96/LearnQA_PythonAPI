import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_json = response.text
response_object = json.loads(response_json)
seconds = response_object["seconds"]
token = response_object["token"]

response_not_ready = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status = json.loads(response_not_ready.text)["status"]
while "Job is NOT ready" in status:
    time.sleep(seconds)
    response_ready = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    response_ready_parsed = json.loads(response_ready.text)
    status = response_ready_parsed["status"]
    result = response_ready_parsed["result"]
    if "Job is ready" in status and result:
        print(status, result)
