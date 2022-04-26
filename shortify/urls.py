"""
URLs for shortify app.
"""
from django.urls import path, re_path

from shortify import views

app_name = 'shortify'

urlpatterns = [
    path('shortify', views.shortify, name='shortify'),
    re_path(r's/(?P<token>[-\w]+)/', views.url_redirect, name='redirect'),
]
