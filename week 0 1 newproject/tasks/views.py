from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
tasklist = ["foo","bar","baz"]
tasklist = []
tasks = ["foo","bar","baz"]
tasks = []

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def removeall(request):
    request.session["tasks"] = []
    # we will simply return to the main page
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def removesome(request):
    request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"] 
            request.session["tasks"] += [task]
            # this will move us back to the back to the page 
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form:": form
            })

    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 10)