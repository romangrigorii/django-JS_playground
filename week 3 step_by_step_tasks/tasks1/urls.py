from urllib.parse import urlparse
from django import urls
from django.urls import path
from . import views

app_name = "tasks1"

urlpatterns = [
    path("", views.index, name="index")
]