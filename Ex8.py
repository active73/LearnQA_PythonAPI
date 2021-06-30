import requests
import time

# Ex8
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()["token"]
seconds = response.json()["seconds"]
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
assert response2.json()["status"] == 'Job is NOT ready', "Job is ready or token is wrong"
time.sleep(seconds)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
assert response3.json()["status"] == 'Job is ready' and response3.json()["result"], "Wrong status or no result"