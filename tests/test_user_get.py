from lib.base_case import BaseCase
from lib.my_requests import MyRequests
from lib.assertions import Assertions
import allure


@allure.epic("Get user cases")
class TestUserGet(BaseCase):

    @allure.description("This is test get user details auth as another user")
    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, 'x-csrf-token')

        response2 = MyRequests.get("/user/1", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_not_key(response2, 'id')
        Assertions.assert_json_has_not_key(response2, 'email')
        Assertions.assert_json_has_not_key(response2, 'firstName')
        Assertions.assert_json_has_not_key(response2, 'lastName')

