from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

# from django.http import HttpResponse
# from .models import *

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.info(request, 'username already exists!')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'email already exists!')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, email=email, password=password)
            user.save()
            return redirect('/login')
        return render(request, "register.html")
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid email or password")
            return redirect('login')        
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')