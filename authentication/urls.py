"""
URLs for the authentication api.
"""
from django.urls import path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from authentication import views as authentication_views

router = DefaultRouter()
router.register(r'user', authentication_views.UserViewSet, basename="user")


urlpatterns = [
    path('login', views.obtain_auth_token, name='api_auth_token'),
    path('register', authentication_views.register_user, name='api_register'),
] + router.urls
