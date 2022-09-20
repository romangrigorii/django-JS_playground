from django.test import TestCase
from django.urls import path
from . import views
# Create your tests here.
app_name = "calculator"

urlpatterns = [
    path("",views.index, name = "index")
]