import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from django.utils import timezone
from django.db import connections
from django.db.utils import OperationalError
from datetime import timedelta

from .forms import SignUpForm
from .models import ErrorLog

logger = logging.getLogger(__name__)


@api_view(["POST"])
def user_signup(request):
    logger.info("Sign-up request received")
    logger.debug(f"Received data: {request.data}")
    form = SignUpForm(request.data)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            auth_login(request._request, user)
            logger.info(f"User {username} registered and logged in successfully")
            return Response(
                {"message": "User registered and logged in successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            logger.warning(f"Authentication failed for user {username}")
            return Response(
                {"errors": "Authentication failed"}, status=status.HTTP_400_BAD_REQUEST
            )
    logger.error("Sign-up form is invalid")
    logger.error(f"Form errors: {form.errors}")
    return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response(
        {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["POST"])
def user_logout(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


def error_count(request):
    one_hour_ago = timezone.now() - timedelta(hours=1)
    count = ErrorLog.objects.filter(
        timestamp__gte=one_hour_ago, status_code__gte=400
    ).count()
    return JsonResponse({"error_count": count})


def health_check(request):
    db_conn = connections["default"]
    try:
        db_conn.cursor()
    except OperationalError:
        return JsonResponse({"status": "unhealthy"}, status=500)
    return JsonResponse({"status": "healthy"})
