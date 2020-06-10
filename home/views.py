from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    main = {}
    return render(request, 'login.html', main)

@login_required(login_url='login') # you can use this '@login_required' to make user must login first, before enter function 
def home(request):
    main = {
            'text':'selamat datang',
            }
    return render(request, 'home.html', main)

def logout_user(request):
    logout(request)
    return redirect('login')



# Create your views here.
