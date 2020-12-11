from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from database.models import Products, SavedProducts
from .form import AccountForm

# Create your views here.

class SignUpView(CreateView):
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    return render(request, 'home.html')

def results_of_research(request):
    return render(request, 'results_of_research.html')

def selected_product(request):
    return render(request, 'selected_product.html')

def account(request):
    return render(request, 'account.html')

def saved_products(request):
    return render(request, 'saved_products.html')

def mentions_legales(request):
    return render(request, 'mentions_legales.html')
