import requests

class TestFirstAPI:
    def test_cookie_method_request(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_value = response.cookies.get('HomeWork')
        assert 'HomeWork' in  response.cookies, 'There is no HomeWork cookie in the response'
        assert cookie_value == 'hw_value', "Value cookie is not 'hw_value'"