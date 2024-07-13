# backend/tests/test_models.py
import pytest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password


@pytest.mark.django_db
def test_create_user(create_user):
    user = create_user(username='testuser', password='password123')
    assert User.objects.count() == 1
    assert user.username == 'testuser'


@pytest.mark.django_db
def test_user_authentication(create_user):
    user = create_user(username='testuser', password='password123')
    authenticated_user = authenticate(username='testuser', password='password123')
    assert authenticated_user is not None
    assert authenticated_user.username == user.username


@pytest.mark.django_db
def test_duplicate_user_creation(create_user):
    create_user(username='testuser', password='password123')
    with pytest.raises(IntegrityError):
        create_user(username='testuser', password='password456')


@pytest.mark.django_db
def test_user_password_hashing(create_user):
    user = create_user(username='testuser', password='password123')
    assert check_password('password123', user.password)
