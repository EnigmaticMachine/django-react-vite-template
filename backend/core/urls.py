from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("error-count/", views.error_count, name="error-count"),
    path("health/", views.health_check, name="health_check"),
    path("test_long_response/", views.test_long_response, name="test_long_response"),

]
