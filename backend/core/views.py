import logging
from datetime import timedelta

from django.contrib.auth import authenticate, login, logout
from django.db import connections
from django.db.utils import OperationalError
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .forms import SignUpForm
from .models import ErrorLog
from .serializers import ErrorLogSerializer, UserSerializer
from rest_framework.exceptions import ValidationError


logger = logging.getLogger(__name__)


class ErrorLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer

    @action(detail=False, methods=["get"])
    def error_count(self, request):
        one_hour_ago = timezone.now() - timedelta(hours=1)
        count = ErrorLog.objects.filter(
            timestamp__gte=one_hour_ago, status_code__gte=400
        ).count()
        return Response({"error_count": count})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def signup(self, request):
        form = SignUpForm(request.data)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "message": "User registered and logged in successfully",
                        "token": token.key,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"errors": "Authentication failed"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"message": "Login successful", "token": token.key},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def token_auth(self, request):
        serializer = ObtainAuthToken.serializer_class(
            data=request.data, context={"request": request}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return Response(
                {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"message": "Login successful", "token": token.key},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class CheckViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def health(self, request):
        db_conn = connections["default"]
        try:
            db_conn.cursor()
        except OperationalError:
            return Response({"status": "unhealthy"}, status=500)
        return Response({"status": "healthy"})

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def test_long_response(self, request):
        data = {"data": ["This is a long response"] * 10}
        return Response(data)
