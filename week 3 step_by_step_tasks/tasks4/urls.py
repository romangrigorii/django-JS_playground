from urllib.parse import urlparse
from django import urls
from django.urls import path
from . import views

app_name = "tasks4" # sets the application namespace

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("reset", views.reset, name = "reset"),
]
