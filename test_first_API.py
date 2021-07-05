import requests
import pytest

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

    # Ex13

    params = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'})
    ]

    @pytest.mark.parametrize('value', params)
    def test_user_agent_check(self, value):
        user_agent, expected_values = value
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": user_agent})
        assert response.json()['platform'] == expected_values['platform'], f"User Agent {user_agent} returned an invalid parameter 'platform'"
        assert response.json()['browser'] == expected_values['browser'], f"User Agent {user_agent} returned an invalid parameter 'browser'"
        assert response.json()['device'] == expected_values['device'], f"User Agent {user_agent} returned an invalid parameter 'device'"
