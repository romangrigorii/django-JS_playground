from queue import PriorityQueue
from socket import fromshare
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse 
taskstodo = ["clean","brush teeth","pet da cat"]

def index(request):
    return render(request, "tasks3/index.html",{
        "tasks": taskstodo # this is the information being provided to the template, so when referencing tasks to do in template files we use 'tasks' variable name isntead
    })
    
def add(request):
    # the code below will be executed when we send information back ti our function 'add'
    if request.method == "POST":
        form = NewTaskForm(request.POST) # note : request.POST contains all  of the submitted data
        if form.is_valid():
            taskstodo.append(form.cleaned_data["task"])
        else:
            return render(request, "tasks3/add.html", {
                "form", form
            })
        return HttpResponseRedirect(reverse("tasks3:index"))
    # the code below will be executed whenever we simply go to our page 'add'
    return render(request, "tasks3/add.html", {
        "form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "NewTask")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
