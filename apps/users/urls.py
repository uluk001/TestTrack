from django.urls import path

from .views import authentication_view, logout, registration_view

urlpatterns = [
    path("login/", authentication_view, name="login"),
    path("registration/", registration_view, name="registration"),
    path("logout/", logout, name="logout"),
]
