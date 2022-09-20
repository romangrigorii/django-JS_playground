from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def roman(request):
    return HttpResponse("Hello Roman")

def chris(request):
    return HttpResponse("Hello Christopher")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

# greet2 function will take a given request and name, use greet.html template for rendering and also take the styling parameters inside {}
def greet2(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() 
    })

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)