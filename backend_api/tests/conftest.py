import django
import pytest
import os
from django.contrib.auth.models import User
from rest_framework.test import APIClient


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def api_client():
    return APIClient()
