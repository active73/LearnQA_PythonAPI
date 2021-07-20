from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.epic("Edit user cases")
class TestUserEdit(BaseCase):
    @allure.description("This is test edit user without authorization")
    def test_edit_user_without_authorization(self):
        # REGISTER
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, 'id')

        # EDIT
        response = MyRequests.put(f"/user/{user_id}", data={"username": 'new_name'})

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == 'Auth token not supplied', 'User edit without authorization'

    @allure.description("This is test edit user auth as another user")
    def test_edit_user_auth_as_another_user(self):
        # REGISTER
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        old_name = register_data['username']
        user_id = self.get_json_value(response1, 'id')

        # AUTH ANOTHER USER
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={"username": new_name}
        )
        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(
            response4,
            "username",
            old_name,
            "Edit name user auth as another user"
        )

    @allure.description("This is test edit user with wrong email")
    def test_edit_user_with_wrong_email(self):
        # REGISTER
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_email = 'learnqatest1examle.com'
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(
            response4,
            "email",
            email,
            "Edit email address to be incorrect"
        )

    def test_edit_user_with_shot_first_name(self):
        # REGISTER
        register_data =self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')
        first_name = register_data['firstName']

        # LOGIN
        data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = 'l'
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            "Edit email address to be incorrect"
        )
