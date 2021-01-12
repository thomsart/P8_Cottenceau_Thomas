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
import requests

import json
from database.models import Products, SavedProducts, ClientUser
from .form import *


# Create your views here.

class SignUpView(CreateView):
    """
    This view
    """
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'






def home(request):
    """
    This view
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
                """
                If this product is not in the database we have to do something to make the user aware
                """
                print("aucun produit n'as été trouvé")

        else:
            print("Non valide")
            product_wanted = SearchProductForm(request.GET)

    return render(request, 'home.html', context)






def selected_product(request, product_id):
    """
    This view
    """
    product = Products.objects.filter(id=product_id).values()
    product = {
        'cat': product[0]['cat'],
        'name': product[0]['name'],
        'brand': product[0]['brand'],
        'store': product[0]['store'],
        'nutriscore': product[0]['nutriscore'],
        'fat_lipids_100g': product[0]['fat_lipids_100g'],
        'saturated_fatty_acids_100g': product[0]['saturated_fatty_acids_100g'],
        'sugar_100g': product[0]['sugar_100g'],
        'salt_100g': product[0]['salt_100g'],
        'photo': product[0]['photo'],
    }
    context = {'product': product}

    return render(request, 'selected_product.html', context)






def proposed_products(request, product_id):
    """
    This view
    """
    product_to_substitute = Products.objects.filter(id=product_id).values()

    all_proposed_products = []
    indices = ['a', 'b', 'c', 'd', 'e']
    for indice in indices:
        if indice == product_to_substitute[0]['nutriscore'] or len(all_proposed_products) == 12:
            break
        else:
            proposed_products = Products.objects.filter(cat=product_to_substitute[0]['cat'],nutriscore=indice).all().values()
            for each_product in proposed_products:
                all_proposed_products.append(each_product)
    print(all_proposed_products)

    context = {
        'product': product_to_substitute[0],
        'substitute_1': all_proposed_products[0],
        'substitute_2': all_proposed_products[1],
        'substitute_3': all_proposed_products[2],
        'substitute_4': all_proposed_products[3],
        'substitute_5': all_proposed_products[4],
        'substitute_6': all_proposed_products[5],
        'substitute_7': all_proposed_products[6],
        'substitute_8': all_proposed_products[7],
        'substitute_9': all_proposed_products[8],
        'substitute_10': all_proposed_products[9],
        'substitute_11': all_proposed_products[10],
        'substitute_12': all_proposed_products[11],
    }

    return render(request, 'proposed_products.html', context)






@login_required
@csrf_exempt
def save_product(request, product_id):
    """
    This view
    """
    if request.method == 'POST':
        id_user_id_product = json.loads(request.body)
        id_user_id_product = id_user_id_product["id"]
        lst = id_user_id_product.split(",")
        userId = ClientUser.objects.get(id=lst[0])
        productId = Products.objects.get(id=lst[1])

        is_product = SavedProducts.objects.filter(product_id=productId.id, user_id=userId.id)

        if is_product:
            print("Ce produit à déjà été sauvegardé")
        else:
            product_to_save = SavedProducts(product_id=productId, user_id=userId)
            product_to_save.save()
            print("Produit enregistré")

    return render(request, 'proposed_products.html')






@login_required
def account(request):
    """
    This view just show all the account details of the user.
    """
    return render(request, 'account.html')






@login_required
def user_substitutes(request):
    """
    This view
    """
    context = {}
    id_login_user = request.user.id
    id_of_all_saved_products = SavedProducts.objects.filter(user_id=id_login_user).values('product_id_id')

    list_of_id = []
    for sets in id_of_all_saved_products:
        list_of_id.append(sets['product_id_id'])
    print(list_of_id)

    for each_id in list_of_id:
        product = Products.objects.filter(id=each_id).values()
        product = {
            'cat': product[0]['cat'],
            'name': product[0]['name'],
            'brand': product[0]['brand'],
            'store': product[0]['store'],
            'nutriscore': product[0]['nutriscore'],
            'fat_lipids_100g': product[0]['fat_lipids_100g'],
            'saturated_fatty_acids_100g': product[0]['saturated_fatty_acids_100g'],
            'sugar_100g': product[0]['sugar_100g'],
            'salt_100g': product[0]['salt_100g'],
            'photo': product[0]['photo'],
        }

        print()

    return render(request, 'user_substitutes.html', context)






def mentions_legales(request):
    """
    This view
    """
    return render(request, 'mentions_legales.html')