from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def page_not_found(request):
    return render(request, 'main_app/404.html')

def trade_room(request):
    return render(request, 'main_app/blog-home-2.html')

def profile(request):
    return render(request, 'main_app/portfolio-item.html')

def creator(request):
    return render(request, 'main_app/test.html')

def login(request):
    return render(request, 'main_app/404.html')
