import pytest
import logging
from django.contrib.auth.models import User
from rest_framework.test import APIClient


logger = logging.getLogger(__name__)


BASE_URL = "http://nginx"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api_client():
    return APIClient()
