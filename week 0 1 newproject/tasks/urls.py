from django import urls
from django.urls import path
from . import views

#  app_name allows us to uniquely tag all the urls 

app_name = "tasks" 

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("removeall", views.removeall, name="removeall"),
    path("removesomme", views.removesome, name="removesome")
]