from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Django Project 2")#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to Homepage<h1>")

def html_demo(request):
    return render(request,"sample.html")

