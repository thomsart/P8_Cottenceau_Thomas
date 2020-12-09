from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

from database.models import Users, Products, SavedProducts
from .login import *

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def results_of_research(request):
    return render(request, 'pages/results_of_research.html')

def selected_product(request):
    return render(request, 'pages/selected_product.html')










def login(request):

    form_login = LoginForm()
    context = {'form_login': form_login}

    if request.method == 'POST':
        e_mail = request.POST['e_mail']
        password = request.POST['password']
        user = authenticate(username=e_mail, password=password)

        if user is not None:
            return redirect("home")
        else:
            messages.error(request, "Erreur d'authentification")
            return render(request, 'pages/login.html', context)

    return render(request, 'pages/login.html', context)








def create_account(request):

    form_account = AccountForm()
    context = {'form_account': form_account}

    if request.method == 'POST':
        form_account = AccountForm(request.POST).save()     # .save() pour les sauvegarder
        return render(request, 'pages/account.html', context)
    else:
        return render(request, 'pages/create_account.html', context)












def account(request):
    return render(request, 'pages/account.html')

def saved_products(request):
    return render(request, 'pages/saved_products.html')

def mentions_legales(request):
    return render(request, 'pages/mentions_legales.html')

def error_404(request):
    return render(request, 'errors/error_404.html')

def error_500(request):
    return render(request, 'errors/error_500.html')