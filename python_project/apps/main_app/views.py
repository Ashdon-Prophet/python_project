from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def faq(request):
    return render(request, 'main_app/faq.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def four(request):
    return render(request, 'main_app/404.html')

def about(request):
    return render(request, 'main_app/about.html')

def blog1(request):
    return render(request, 'main_app/blog-home-1.html')

def blog2(request):
    return render(request, 'main_app/blog-home-2.html')

def blog_post(request):
    return render(request, 'main_app/blog-post.html')

def portfolio_item(request):
    return render(request, 'main_app/portfolio-item.html')

def portfolio1(request):
    return render(request, 'main_app/portfolio-1-col.html')

def portfolio2(request):
    return render(request, 'main_app/portfolio-2-col.html')

def portfolio3(request):
    return render(request, 'main_app/portfolio-3-col.html')

def portfolio4(request):
    return render(request, 'main_app/portfolio-4-col.html')

def pricing(request):
    return render(request, 'main_app/pricinghtml')

def services(request):
    return render(request, 'main_app/services.html')

def sidebar(request):
    return render(request, 'main_app/sidebar.html')

def full_width(request):
    return render(request, 'main_app/full-width.html')
