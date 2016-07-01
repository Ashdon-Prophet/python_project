from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Creature

def index(request):
    return render(request, 'main_app/index.html')

def page_not_found(request):
    return render(request, 'main_app/404.html')

def trade_room(request):
    creatures = Creature.objects.all()
    context = {
        'creatures': creatures
    }
    return render(request, 'main_app/blog-home-2.html', context)

def profile(request):
    user = User.userManager.get(username=request.session['username'])
    return render(request, 'main_app/portfolio-item.html', {'user': user})

def creator(request):
    request.session['head'] = 'normal'
    request.session['bod'] = 'paleblackbody'
    request.session['legs'] = 'bluepants'
    request.session['arms'] = 'palebluet'
    return render(request, 'main_app/creator.html')

def loginandreg(request):
    return render(request, 'main_app/login.html')

def trade(request, id):
    creature = Creature.objects.get(id=id)
    all_creatures = Creature.objects.all()
    context = {
        'creature': creature,
        'all_creatures': all_creatures
        }
    return render(request, 'main_app/pricing.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def process_register(request):
    if request.method == 'POST':
        new_user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['username'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
        if new_user:
            for key, error in new_user.iteritems():
                messages.error(request, error)
            return redirect('/login')
        return redirect('/login')

def process_login(request):
    if request.method == 'POST':
        try:
            user = User.userManager.login(request.POST['email'], request.POST['password'])
            request.session['id'] = user[1].id
            request.session['username'] = user[1].username
            request.session['first_name'] = user[1].first_name
            request.session['last_name'] = user[1].last_name
            request.session['username'] = user[1].username
            request.session['description'] = user[1].description
            request.session['owned'] = user[1].owned
            request.session['traded'] = user[1].traded
            request.session['number_created'] = user[1].number_created
            request.session['email'] = user[1].email
            return redirect('/profile')
        except:
            return redirect('/login')

def process_trade(request):
    return render(request, 'main_app/pricing.html')

def process_create(request):
    if request.method == 'POST':
        owner = User.userManager.get(id=request.session['id'])
        ceature = Creature.objects.create(name = request.POST['creature_name'], description = request.POST['description'], head_style = request.POST['head'], body_style = request.POST['body'], arm_style = request.POST['arms'], leg_style = request.POST['legs'], owner = owner)
        owner.owned += 1
        owner.number_created += 1
        owner.save()
        return redirect('/profile')
