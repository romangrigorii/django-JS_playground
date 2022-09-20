from django.shortcuts import render
import datetime


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    # now.month = 1
    # now.day = 1
    return render(request, "newyear/index.html", {
        "newyear":  now.month == 1 and now.day == 1,
        "secondyear":  now.month == 9 and now.day == 1
    })
     