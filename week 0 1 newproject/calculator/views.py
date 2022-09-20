from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

storedvals = []

def index(request):
    return render(request,"index.html")

def test_view(request):
    if request.method == 'POST':
        form = Fooform(request.POST)
        if form.is_valid():
            val = form.cleaned_data["val"]
            storedvals += val
    else:
        form = Fooform()
    return render(request, '{% url calcualtor:index%} ', locals())

class Fooform(forms.Form):
    val = forms.CharField()