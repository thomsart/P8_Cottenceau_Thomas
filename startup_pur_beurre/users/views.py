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


# def login(request):

#     form_login = LoginForm()
#     context = {'form_login': form_login}

#     if request.method == 'POST':
#         e_mail = request.POST['e_mail']
#         password = request.POST['password']
#         user = authenticate(username=e_mail, password=password)

#         if user is not None:
#             return redirect("home")
#         else:
#             messages.error(request, "Erreur d'authentification")
#             return render(request, 'registration/login.html', context)

#     return render(request, 'registration/login.html', context)

# def signup(request):

#     form_account = AccountForm()
#     context = {'form_account': form_account}

#     if request.method == 'POST':
#         form_account = AccountForm(request.POST).save()     # .save() pour les sauvegarder
#         return render(request, 'account.html', context)
#     else:
#         return render(request, 'registration/signup.html', context)


def account(request):
    return render(request, 'account.html')

def saved_products(request):
    return render(request, 'saved_products.html')

def mentions_legales(request):
    return render(request, 'mentions_legales.html')

def error_404(request):
    return render(request, 'error_404.html')

def error_500(request):
    return render(request, 'error_500.html')