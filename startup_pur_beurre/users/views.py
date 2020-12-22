#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
            print(product)
            print("\n\n\n")

            if product:
                product_id = product[0]['id']
                product_id = int(product_id)

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

    product = Products.objects.filter(id=product_id).values()

    def substitute(substitute, substitute_nb):

        features = {
            'id' : substitute[substitute_nb]['id'],
            'cat' : substitute[substitute_nb]['cat'],
            'name' : substitute[substitute_nb]['name'],
            'brand' : substitute[substitute_nb]['brand'],
            'store' : substitute[substitute_nb]['store'],
            'nutriscore' : substitute[substitute_nb]['nutriscore'],
            'fat_lipids_100g' : substitute[substitute_nb]['fat_lipids_100g'],
            'saturated_fatty_acids_100g' : substitute[substitute_nb]['saturated_fatty_acids_100g'],
            'sugar_100g' : substitute[substitute_nb]['sugar_100g'],
            'salt_100g' : substitute[substitute_nb]['salt_100g'],
            'photo' : substitute[substitute_nb]['photo'],
        }

        return features

    all_proposed_products = []
    indices = ['a', 'b', 'c', 'd', 'e']
    i = 0
    while i < 5:
        if indices[i] == product[0]['nutriscore']:
            i = 5
        else:
            proposed_products = Products.objects.filter(cat=product[0]['cat'],nutriscore=indices[i]).all().values()
            for el in proposed_products:
                all_proposed_products.append(el)
            i += 1

    # print(all_proposed_products)

    list_of_substitutes = []
    i = 0
    for each_product in all_proposed_products:
        if i == 6:
            break
        else:
            list_of_substitutes.append(substitute(all_proposed_products, i))
            i += 1

    # print(list_of_substitutes)

    context = {
        'product': product[0],
        'substitute_1': list_of_substitutes[0],
        'substitute_2': list_of_substitutes[1],
        'substitute_3': list_of_substitutes[2],
        'substitute_4': list_of_substitutes[3],
        'substitute_5': list_of_substitutes[4],
        'substitute_6': list_of_substitutes[5],
    }

    return render(request, 'proposed_products.html', context)





















def account(request):
    """
    This view
    """


    return render(request, 'account.html')


def saved_products(request):
    """
    This view
    """


    return render(request, 'saved_products.html')


def mentions_legales(request):
    """
    This view
    """


    return render(request, 'mentions_legales.html')






# product = {
#         'id': product[0]['id'],
#         'cat': product[0]['cat'],
#         'name': product[0]['name'],
#         'brand': product[0]['brand'],
#         'store': product[0]['store'],
#         'nutriscore': product[0]['nutriscore'],
#         'fat_lipids_100g': product[0]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': product[0]['saturated_fatty_acids_100g'],
#         'sugar_100g': product[0]['sugar_100g'],
#         'salt_100g': product[0]['salt_100g'],
#         'photo': product[0]['photo'],
#     }
# substitute_1 = {
#         'id': products[0]['id'],
#         'cat': products[0]['cat'],
#         'name': products[0]['name'],
#         'brand': products[0]['brand'],
#         'store': products[0]['store'],
#         'nutriscore': products[0]['nutriscore'],
#         'fat_lipids_100g': products[0]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': products[0]['saturated_fatty_acids_100g'],
#         'sugar_100g': products[0]['sugar_100g'],
#         'salt_100g': products[0]['salt_100g'],
#         'photo': products[0]['photo'],
#     }
#     substitute_2 = {
#         'id': products[1]['id'],
#         'cat': products[1]['cat'],
#         'name': products[1]['name'],
#         'brand': products[1]['brand'],
#         'store': products[1]['store'],
#         'nutriscore': products[1]['nutriscore'],
#         'fat_lipids_100g': products[1]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': products[1]['saturated_fatty_acids_100g'],
#         'sugar_100g': products[1]['sugar_100g'],
#         'salt_100g': products[1]['salt_100g'],
#         'photo': products[1]['photo'],
#     }
#     substitute_3 = {
#         'id': products[2]['id'],
#         'cat': products[2]['cat'],
#         'name': products[2]['name'],
#         'brand': products[2]['brand'],
#         'store': products[2]['store'],
#         'nutriscore': products[2]['nutriscore'],
#         'fat_lipids_100g': products[2]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': products[2]['saturated_fatty_acids_100g'],
#         'sugar_100g': products[2]['sugar_100g'],
#         'salt_100g': products[2]['salt_100g'],
#         'photo': products[2]['photo'],
#     }
#     substitute_4 = {
#         'id': products[3]['id'],
#         'cat': products[3]['cat'],
#         'name': products[3]['name'],
#         'brand': products[3]['brand'],
#         'store': products[3]['store'],
#         'nutriscore': products[3]['nutriscore'],
#         'fat_lipids_100g': products[3]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': products[3]['saturated_fatty_acids_100g'],
#         'sugar_100g': products[3]['sugar_100g'],
#         'salt_100g': products[3]['salt_100g'],
#         'photo': products[3]['photo'],
#     }
#     substitute_5 = {
#         'id': products[4]['id'],
#         'cat': products[4]['cat'],
#         'name': products[4]['name'],
#         'brand': products[4]['brand'],
#         'store': products[4]['store'],
#         'nutriscore': products[4]['nutriscore'],
#         'fat_lipids_100g': products[4]['fat_lipids_100g'],
#         'saturated_fatty_acids_100g': products[4]['saturated_fatty_acids_100g'],
#         'sugar_100g': products[4]['sugar_100g'],
#         'salt_100g': products[4]['salt_100g'],
#         'photo': products[4]['photo'],
#     }
    # substitute_6 = {
    #     'id': products[5]['id'],
    #     'cat': products[5]['cat'],
    #     'name': products[5]['name'],
    #     'brand': products[5]['brand'],
    #     'store': products[5]['store'],
    #     'nutriscore': products[5]['nutriscore'],
    #     'fat_lipids_100g': products[5]['fat_lipids_100g'],
    #     'saturated_fatty_acids_100g': products[5]['saturated_fatty_acids_100g'],
    #     'sugar_100g': products[5]['sugar_100g'],
    #     'salt_100g': products[5]['salt_100g'],
    #     'photo': products[5]['photo'],
    # }