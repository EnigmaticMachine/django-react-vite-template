from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='api_login'),
    path('logout/', views.user_logout, name='api_logout'),
]
