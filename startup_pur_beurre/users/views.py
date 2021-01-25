#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import requests

import json
from database.models import Products, SavedProducts, ClientUser
from .form import *
from . import context_processor

# Create your views here.

################################################################################

class SignUpView(CreateView):
    """
    This view allows the user to login or create an account.
    """
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

################################################################################

def home(request):
    """
    This view just generate the home-page and listen GET requests from the two
    forms.
    """
    product_wanted = SearchProductForm(request.GET)
    context = {'search_product': product_wanted}

    if request.method == 'GET':

        if product_wanted.is_valid():
            product_name = product_wanted.cleaned_data['product_name']
            product = Products.objects.filter(name__iexact=product_name).values()

            if product:
                product_id = int(product[0]['id'])

                return redirect('selected_product/', product_id=product_id)

            else:
                messages.info(request, "Aucun produit n'a été trouvé, Vérifie que l'orthographe est la bonne !")

        else:
            product_wanted = SearchProductForm(request.GET)

    return render(request, 'home.html', context)

################################################################################

def search_product(request):
    """
    This view present the product the user wants to substitute.
    """
    # template = loader.get_template("users/base.html")

    query = request.POST.get("product_name_nav_bar")
    
    product = Products.objects.filter(name__iexact=query).values()
    if product:
        product_id = int(product[0]['id'])
        return redirect('selected_product/', product_id=product_id)

    else:
        messages.info(request, "Aucun produit n'a été trouvé, Vérifie que l'orthographe est la bonne !")
        return redirect('home')


################################################################################

def selected_product(request, product_id):
    """
    This view present the product the user wants to substitute.
    """
    product = Products.objects.filter(id=product_id).all().values()

    context = {
        'product': product,
    }

    return render(request, 'selected_product.html', context)

################################################################################

def proposed_products(request, product_id):
    """
    This view shows to the user all the healthier products that could replace
    the product.
    """
    product_to_substitute = Products.objects.filter(id=product_id).values()

    all_proposed_products = []
    indices = ['a', 'b', 'c', 'd', 'e']
    for indice in indices:
        if indice == product_to_substitute[0]['nutriscore']:
            break
        else:
            proposed_products = Products.objects.filter(
                                cat=product_to_substitute[0]['cat'],
                                nutriscore=indice).all().values()
            for each_product in proposed_products:
                if each_product['store'] == '':
                    continue
                else:
                    all_proposed_products.append(each_product)

    context = {
        'products': all_proposed_products,
    }

    return render(request, 'proposed_products.html', context)

################################################################################

@login_required
@csrf_exempt
def save_product(request, product_id):
    """
    This view allows the user to save products if he wants. This required of
    course from him to register to the site.  
    """
    if request.method == 'POST':
        productId = json.loads(request.body)
        productId = productId["id"]
        id_product = Products.objects.get(id=productId)
        userId = request.user.id
        id_login_user = ClientUser.objects.get(id=userId)

        is_product = SavedProducts.objects.filter(product_id=id_product,
                        user_id=id_login_user)

        if is_product:
            pass
        else:
            product_to_save = SavedProducts(product_id=id_product,
                                user_id=id_login_user)
            product_to_save.save()

    return render(request, 'proposed_products.html')

################################################################################

@login_required
def user_substitutes(request):
    """
    In this view the user can see all his substitutes.
    """
    id_login_user = request.user.id
    all_id_of_saved_products = SavedProducts.objects.filter(
                            user_id=id_login_user).all().values('product_id_id')
    
    all_ids = []
    for id_save_product in all_id_of_saved_products:
        for key, value in id_save_product.items():
            all_ids.append(value)

    list_of_saved_products = []
    for each_id in all_ids:
        product = Products.objects.filter(id=each_id).all().values()
        list_of_saved_products.append(product[0])

    context = {
        'products': list_of_saved_products,
    }

    return render(request, 'user_substitutes.html', context)

################################################################################

@login_required
def delete_product(request, product_id):
    """
    This view allows the user to delete from his account a product he saved.
    """
    id_login_user = request.user.id
    SavedProducts.objects.filter(user_id=id_login_user,
    product_id=product_id).delete()

    return redirect('user_substitutes/')

################################################################################

@login_required
def account(request):
    """
    This view just show all the account details of the user like his name and
    e-mail for exemple.
    """
    return render(request, 'account.html')

################################################################################

def mentions_legales(request):
    """
    This view just shows the Legales-Mentions of the site.
    """
    return render(request, 'mentions_legales.html')
