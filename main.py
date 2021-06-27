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


# Ex7
# 1
method={}
response1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
response2 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
response3 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
print(f"Ответ на post-запрос без параметра method: {response1.text} \n"
      f"Ответ на put-запрос без параметра method: {response2.text} \n"
      f"Ответ на delete-запрос без параметра method: {response3.text} \n"
      f"Ответ на get-запрос без параметра method: {response4.text}")

# 2
response5 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print(f"Ответ на запрос не из списка: {response5.text}")

# 3-4
methods = [{"method": "GET"}, {"method": "PUT"}, {"method": "POST"}, {"method": "DELETE"}]

for method in methods:
    response6 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    print(f"Ответ на get-запрос с методом {method['method']}: {response6.text}")
    response7 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"Ответ на post-запрос с методом {method['method']}: {response7.text}")
    response8 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"Ответ на put-запрос с методом {method['method']}: {response8.text}")
    response9 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"Ответ на delete-запрос с методом {method['method']}: {response9.text}")