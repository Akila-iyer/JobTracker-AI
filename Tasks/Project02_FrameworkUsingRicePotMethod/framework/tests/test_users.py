import pytest
from api_client import APIClient
import sys
sys.path.insert(0, '..')
from test_data.users_data import users

class TestUserAPI:
    def setup_class(self):
        self.api = APIClient()

    @pytest.mark.parametrize("user", users)
    def test_create_user_positive(self, user):
        response = self.api.post("/users", json=user)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_user_negative_empty_payload(self):
        response = self.api.post("/users", json={})
        assert response.status_code == 400

    def test_create_user_negative_missing_name(self):
        response = self.api.post("/users", json={"job": "Engineer"})
        assert response.status_code == 400

class TestUserCRUD:
    def setup_class(self):
        self.api = APIClient()
        self.login_data = {"email": "eve.holt@reqres.in", "password": "123456"}
        self.invalid_login = {"email": "invalid@test.com", "password": "wrong"}

    def test_login_positive(self):
        response = self.api.post("/login", json=self.login_data)
        assert response.status_code == 200
        assert "token" in response.json()

    def test_login_negative(self):
        response = self.api.post("/login", json=self.invalid_login)
        assert response.status_code == 400

    def test_get_users(self):
        response = self.api.get("/users?page=2")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_get_users_negative_invalid_page(self):
        response = self.api.get("/users?page=abc")
        assert response.status_code == 400