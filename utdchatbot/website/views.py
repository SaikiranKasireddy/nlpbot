from django.shortcuts import render
from django.urls import path


# Create your views here.

def homepage(request):
    return render(request, 'website/index.html')