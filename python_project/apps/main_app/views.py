from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'main_app/index.html')

def page_not_found(request):
    return render(request, 'main_app/404.html')

def trade_room(request):
    return render(request, 'main_app/blog-home-2.html')

def profile(request):
    user = User.userManager.get(username=request.session['username'])
    print user
    return render(request, 'main_app/portfolio-item.html', {'user': user})

def creator(request):
    return render(request, 'main_app/creator.html')

def loginandreg(request):
    return render(request, 'main_app/login.html')

def process_register(request):
    if request.method == 'POST':
        new_user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['username'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
        if new_user:
            for key, error in new_user.iteritems():
                messages.error(request, error)
            return redirect('/login')
        request.session['username'] = request.POST['username']
        request.session['first_name'] = request.POST['first_name']
        return redirect('/profile')

def process_login(request):
    if request.method == 'POST':
        try:
            user = User.userManager.login(request.POST['email'], request.POST['password'])
            request.session['username'] = user[1].username
            request.session['first_name'] = user[1].first_name
            return redirect('/profile')
        except:
            return redirect('/login')
