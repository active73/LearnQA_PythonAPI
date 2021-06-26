import requests
import json

# Ex5
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
print(obj)


# Ex6
response = requests.get("https://playground.learnqa.ru/api/long_redirect")
result = response.history
print(list(map(lambda x: x.url, result)))
