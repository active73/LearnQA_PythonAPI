from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic("Delete cases")
class TestUserDelete(BaseCase):
    @allure.description("This is test delete user with id=2")
    def test_delete_user_with_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, 'x-csrf-token')
        user_id = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.delete(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        Assertions.assert_code_status(response2, 400)

        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

    @allure.description("This is test delete user with authorization")
    def test_delete_user_with_auth(self):
        # REGISTER
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']

        # LOGIN
        data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')
        user_id = self.get_json_value(response2, 'user_id')

        # DELETE
        response3 = MyRequests.delete(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        Assertions.assert_code_status(response2, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode('utf-8') == 'User not found', 'User is not deleted'

    @allure.description("This is test delete user auth as another user")
    def test_delete_user_auth_as_another_user(self):
        # REGISTER1
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id1 = self.get_json_value(response1, 'id')

        # REGISTER2
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']

        # LOGIN2
        data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # DELETE
        response3 = MyRequests.delete(f"/user/{user_id1}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        # GET
        response4 = MyRequests.get(f"/user/{user_id1}")

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "username")
