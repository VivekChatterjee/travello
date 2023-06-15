from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST': 
        username=request.POST.get('username')
        password=request.POST.get('password1')

        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password1, email=email)
                user.save()
                print('User Created')
                return redirect('login')
        else:
                messages.info(request,'Password Unmatched')
                return redirect('register')


    else:
        print(User)
        return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
