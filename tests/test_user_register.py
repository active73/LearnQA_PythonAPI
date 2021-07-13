import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest

class TestUserRegister(BaseCase):

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    def test_create_user_with_wrong_email(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'learnqaexample.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == 'Invalid email format', 'User create with wrong email'

    params = [
        ({'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'learnqa@example.com'}, 'password'),
        ({'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'learnqa@example.com'}, 'username'),
        ({'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'learnqa@example.com'}, 'firstName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'learnqa@example.com'}, 'lastName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}, 'email')
    ]

    @pytest.mark.parametrize('param', params)
    def test_create_user_without_parameter(self, param):
        data, missing_parameter = param

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"The following required params are missed: {missing_parameter}"

    def test_create_user_with_shot_first_name(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': 'learnqa@example.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'firstName' field is too short", 'User create with shot firstName'

    def test_create_user_with_long_first_name(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'hrfhhyrylnhytnfhhgrhjhytelnhyrhtkrlshtrwhyjytwjkbjhkvkvgbjkjbvligtrwhyhytjhytejnytejnytednyhtdgntdgvfeabtabhtgabsnbtgrfntgrfsntgrfsntgrfsntgrsfntgrsntrsntrsntrsntrsntgrsntgrsntgsntgrsfntgfsnbgfngfnyhnmgbrghtrsnjhynyfsngtfstsrhtrsnjnyutdngfsbfedaeawerg',
            'lastName': 'learnqa',
            'email': 'learnqa@example.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'firstName' field is too long", 'User create with long firstName'
