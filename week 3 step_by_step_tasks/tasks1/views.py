from django.shortcuts import render


taskstodo = ["clean","brush teeth","pet da cat"]

def index(request):
    return render(request, "tasks1/index.html",{
        "tasks": taskstodo # this is the information being provided to the template
    })
    