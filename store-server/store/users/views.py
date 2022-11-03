from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm,UserRegistationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request,'users/login.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistationForm()
    form = UserRegistationForm()
    context = {'form':form}
    return render(request,'users/register.html',context)