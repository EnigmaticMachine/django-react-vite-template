import django
import pytest
import logging
from django.contrib.auth.models import User
from rest_framework.test import APIClient

logger = logging.getLogger(__name__)


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api_client():
    return APIClient()
