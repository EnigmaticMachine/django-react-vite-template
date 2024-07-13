import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_signup(api_client):
    url = reverse("core:signup")
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
    user = create_user(username="testuser", password="testpassword123")
    url = reverse("core:login")
    data = {"username": "testuser", "password": "testpassword123"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Login successful"


@pytest.mark.django_db
def test_user_login_invalid(api_client):
    url = reverse("core:login")
    data = {"username": "nonexistentuser", "password": "wrongpassword"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["message"] == "Invalid credentials"


@pytest.mark.django_db
def test_user_logout(api_client, create_user):
    user = create_user(username="testuser", password="testpassword123")
    api_client.login(username="testuser", password="testpassword123")
    url = reverse("core:logout")
    response = api_client.post(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Logout successful"
