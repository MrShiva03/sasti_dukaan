from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')

def logout_view(request):
    return render(request,'home.html')

def seller_login_view(request):
    return render(request,'accounts/seller/login.html')

def seller_register_view(request):
    return render(request,'accounts/seller/register.html')

def seller_forgot_pass_view(request):
    return render(request,'accounts/seller/forget_password.html')
#customer
def customer_login_view(request):
    return render(request,'accounts/customer/login.html')

def customer_register_view(request):
    return render(request,'accounts/customer/register.html')

def customer_forgot_pass_view(request):
    return render(request,'accounts/customer/forget_password.html')


