import pytest
from rest_framework import status


@pytest.mark.django_db
def test_user_signup_and_login(api_client):
    signup_url = "/api/users/signup/"
    signup_data = {
        "username": "testuser",
        "password1": "testpassword123",
        "password2": "testpassword123",
        "email": "testuser@example.com",
    }
    signup_response = api_client.post(signup_url, signup_data, format="json")
    assert signup_response.status_code == status.HTTP_201_CREATED

    login_url = "/api/users/login/"
    login_data = {"username": "testuser", "password": "testpassword123"}
    login_response = api_client.post(login_url, login_data, format="json")
    assert login_response.status_code == status.HTTP_200_OK
    assert login_response.data["message"] == "Login successful"
