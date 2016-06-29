from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
    user_dict = {
        'users': User.userManager.all()
        }
    return render(request, 'main_app/test.html', user_dict)

def register(request):
    if request.method == 'POST':
        new_user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['username'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
        if new_user:
            for key, error in new_user.iteritems():
                messages.error(request, error)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        try:
            user = User.userManager.login(request.POST['email'], request.POST['password'])
            request.session['id'] = user[1].id
            request.session['first_name'] = user[1].first_name
            return render(request, 'main_app/success.html')
        except:
            return redirect('/')