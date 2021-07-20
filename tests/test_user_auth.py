import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
       data = {
           'email': 'vinkotov@example.com',
           'password': '1234'
       }
       response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

       self.auth_sid = self.get_cookie(response1, 'auth_sid')
       self.token = self.get_header(response1, 'x-csrf-token')
       self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')

    @allure.description("This is test successfully authorize user by email and password")
    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "user id from auth method is not equal to user id from check method"
        )
