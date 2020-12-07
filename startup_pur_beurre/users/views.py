from django.shortcuts import render

from database.models import Users, Products, SavedProducts
from .login import *

# Create your views here.

def login(request):
    form_login = UserForm()
    context = {'form': form_login}

    # la je ferai mes conditions en fonction des vérifications dans la base de donnée

    return render(request, 'pages/login.html', context)

def create_account(request):
    form_account = AccountForm()
    context = {'form': form_account}
    return render(request, 'pages/create_account.html', context)

def account(request):
    return render(request, 'pages/account.html')

def saved_products(request):
    return render(request, 'pages/saved_products.html')
