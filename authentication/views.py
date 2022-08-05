import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# neha user admin psw Abhumi@123
# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created!..")
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        User= authenticate(username=username, password=pass1)
        if User:
            login(request,User)
            fname=User.first_name
            return render(request,"authentication/dashboard.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!..")
            return redirect('/home')

    return render(request, "authentication/signin.html")

def signout(request):
    return render(request, "authentication/index.html")

