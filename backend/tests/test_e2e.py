import pytest
import requests
import logging


logger = logging.getLogger(__name__)

BASE_URL = "http://nginx"

signup_data = {
    "username": "testuser_e2e",
    "password1": "testpassword123",
    "password2": "testpassword123",
    "email": "testuser_e2e@example.com",
}
login_data = {"username": "testuser_e2e", "password": "testpassword123"}


def test_health_endpoint():
    health_url = f"{BASE_URL}/api/health/"
    response = requests.get(health_url)

    logger.debug("Response status code: %s", response.status_code)
    logger.debug("Response content: %s", response.content)

    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"
    assert (
        response.json().get("status") == "healthy"
    ), f"Expected status 'healthy', got {response.json().get('status')}"
    print("Health endpoint test passed")


def test_leng_response_gzip():
    health_url = f"{BASE_URL}/api/test_long_response/"
    headers = {"Accept-Encoding": "gzip"}
    response = requests.get(health_url, headers=headers)

    logger.debug("Gzip Response status code: %s", response.status_code)
    logger.debug("Gzip Response headers: %s", response.headers)
    logger.debug("Gzip Response content: %s", response.content)

    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"
    assert (
        response.headers.get("Content-Encoding") == "gzip"
    ), f"Expected Content-Encoding 'gzip', got {response.headers.get('Content-Encoding')}"
    print("Health endpoint gzip test passed")


def test_leng_response_brotli():
    health_url = f"{BASE_URL}/api/test_long_response/"
    headers = {"Accept-Encoding": "br"}
    response = requests.get(health_url, headers=headers)

    logger.debug("Brotli Response status code: %s", response.status_code)
    logger.debug("Brotli Response headers: %s", response.headers)
    logger.debug("Brotli Response content: %s", response.content)

    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"
    assert (
        response.headers.get("Content-Encoding") == "br"
    ), f"Expected Content-Encoding 'br', got {response.headers.get('Content-Encoding')}"
    print("Health endpoint brotli test passed")


@pytest.mark.django_db
def test_user_signup():
    url = f"{BASE_URL}/api/signup/"
    response = requests.post(url, json=signup_data)

    logger.debug("Sign up Response status code: %s", response.status_code)
    logger.debug("Sign up Response content: %s", response.content)

    assert (
        response.status_code == 201
    ), f"Expected status code 201, got {response.status_code}"
    assert response.json()["message"] == "User registered and logged in successfully"
    logger.info("User signup test passed")


def test_user_login():
    login_url = f"{BASE_URL}/api/login/"
    login_response = requests.post(login_url, json=login_data)

    logger.debug("Login Response status code: %s", login_response.status_code)
    logger.debug("Login Response content: %s", login_response.content)

    assert (
        login_response.status_code == 200
    ), f"Expected status code 200, got {login_response.status_code}"
    assert login_response.json()["message"] == "Login successful"
    print("User login test passed")


def test_user_login_invalid():
    url = f"{BASE_URL}/api/login/"
    data = {"username": "nonexistentuser", "password": "wrongpassword"}
    response = requests.post(url, json=data)
    assert (
        response.status_code == 400
    ), f"Expected status code 400, got {response.status_code}"
    assert response.json()["message"] == "Invalid credentials"
    print("Invalid user login test passed")


def test_user_logout():
    login_url = f"{BASE_URL}/api/login/"
    login_response = requests.post(login_url, json=login_data)
    assert (
        login_response.status_code == 200
    ), f"Expected status code 200, got {login_response.status_code}"

    # Get the token from the login response
    token = login_response.json().get("token")

    # Now, log out the user
    logout_url = f"{BASE_URL}/api/logout/"
    headers = {"Authorization": f"Token {token}"}
    logout_response = requests.post(logout_url, headers=headers)
    assert (
        logout_response.status_code == 200
    ), f"Expected status code 200, got {logout_response.status_code}"
    assert logout_response.json()["message"] == "Logout successful"
    print("User logout test passed")
