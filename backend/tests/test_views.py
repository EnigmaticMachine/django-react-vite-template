import pytest
from rest_framework import status
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_signup(api_client):
    url = "/api/users/signup/"
    data = {
        "username": "testuser",
        "password1": "testpassword123",
        "password2": "testpassword123",
        "email": "testuser@example.com",
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "User registered and logged in successfully"
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_login(api_client, create_user):
    create_user(username="testuser", password="testpassword123")
    url = "/api/users/login/"
    data = {"username": "testuser", "password": "testpassword123"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Login successful"


@pytest.mark.django_db
def test_user_login_invalid(api_client):
    url = "/api/users/login/"
    data = {"username": "nonexistentuser", "password": "wrongpassword"}
    response = api_client.post(url, data, format="json")

    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), f"Expected status code 400, got {response.status_code}"
    assert (
        "message" in response.json()
    ), f"Expected 'message' in response, got {response.json()}"
    assert (
        response.json()["message"] == "Invalid credentials"
    ), f"Expected message 'Invalid credentials', got {response.json()['message']}"


@pytest.mark.django_db
def test_user_logout(api_client, create_user):
    create_user(username="testuser", password="testpassword123")
    login_url = "/api/users/login/"
    login_data = {"username": "testuser", "password": "testpassword123"}
    login_response = api_client.post(login_url, login_data, format="json")
    assert (
        login_response.status_code == status.HTTP_200_OK
    ), f"Expected status code 200, got {login_response.status_code}"

    token = login_response.data.get("token")
    assert token is not None, "Token should not be None"
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    logout_url = "/api/users/logout/"
    logout_response = api_client.post(logout_url, format="json")

    assert (
        logout_response.status_code == status.HTTP_200_OK
    ), f"Expected status code 200, got {logout_response.status_code}"
    assert logout_response.data["message"] == "Logout successful"
    print("User logout test passed")
