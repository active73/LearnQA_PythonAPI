import requests

class TestFirstAPI:
    def test_cookie_method_request(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_value = response.cookies.get('HomeWork')
        assert 'HomeWork' in  response.cookies, 'There is no HomeWork cookie in the response'
        assert cookie_value == 'hw_value', "Value cookie is not 'hw_value'"

    # Ex12
    def test_header_method_request(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header_value = response.headers.get('x-secret-homework-header')
        assert 'x-secret-homework-header' in response.headers, 'There is no x-secret-homework-header in the response'
        assert header_value == 'Some secret value', "Value header is not equal to 'Some secret value'"