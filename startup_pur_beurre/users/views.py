from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from database.models import Products, SavedProducts
from .form import *

# Create your views here.

class SignUpView(CreateView):

    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):

    product_wanted = SearchProductForm(request.POST)
    context = {'search_product': product_wanted}

    if request.method == 'POST':
        if product_wanted.is_valid():
            product_name = product_wanted.cleaned_data['product_name']
            print(product_name)

            product_from_db = Products.objects.filter(name=product_name).values()

            if product_from_db[0]['name'] != None:
                # we send it to the page 'results_of_research'
                print("On y est la")
                print(product_from_db[0])
                pass
            else:
                print("Ce produit n'est pas référencé")
                # return HttpResponseRedirect('results_of_research.html') 
                

        else:
            product_wanted = SearchProductForm()

    return render(request, 'home.html', context)


def results_of_research(request, HttpResponse):


    return render(request, 'results_of_research.html')


def selected_product(request):
    return render(request, 'selected_product.html')


def account(request):
    return render(request, 'account.html')


def saved_products(request):
    return render(request, 'saved_products.html')


def mentions_legales(request):
    return render(request, 'mentions_legales.html')
