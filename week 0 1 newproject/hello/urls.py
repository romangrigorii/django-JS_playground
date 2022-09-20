from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("roman", views.roman, name = "roman"),
    path("chris", views.chris, name = "chris"),
    path("time", views.current_datetime, name= "time"),
    path("<str:name>", views.greet2, name= "greet")    
]