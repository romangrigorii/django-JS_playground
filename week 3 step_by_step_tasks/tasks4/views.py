from queue import PriorityQueue
from socket import fromshare
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse 

def index(request):
    # this checks if the variable 'tasks' is in the user's session and if it is not it initializes it. This is a way to create variables that are unique to a given session and are not the same across users
    if "tasks" not in request.session: 
        request.session["tasks"] = ["clean","brush teeth","pet da cat"]

    return render(request, "tasks4/index.html",{
        "tasks": request.session["tasks"] # this is the information being provided to the template, so when referencing tasks to do in template files we use 'tasks' variable name isntead
    })
    
def add(request):
    # the code below will be executed when we send information back to our function 'add'
    if request.method == "POST":
        form = NewTaskForm(request.POST) # note : request.POST contains all  of the submitted data
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task not in request.session["tasks"]:
                request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks4:index"))
        else:
            return render(request, "tasks4/add.html", {
                "form", form
            })      
    # the code below will be executed whenever we simply go to our page 'add'
    return render(request, "tasks4/add.html", {
        "form": NewTaskForm()
    })

def reset(request):
    request.session["tasks"] = []
    return HttpResponseRedirect(reverse("tasks4:index"))

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "NewTask")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

