from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def faq(request):
    return render(request, 'main_app/faq.html')

def blog(request):
    return render(request, 'main_app/blog.html')

def contact(request):
    return render(request, 'main_app/contact.html')
