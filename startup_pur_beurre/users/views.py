from django.shortcuts import render

from database.models import Users, Products, SavedProducts
from display import login

# Create your views here.

def account(request):
    return render(request, 'pages/account.html')

def saved_products(request):
    return render(request, 'pages/saved_products.html')
