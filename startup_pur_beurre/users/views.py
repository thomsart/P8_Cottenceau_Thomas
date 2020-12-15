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

    product_wanted = SearchProductForm(request.POST)
    context = {'search_product': product_wanted}

    if request.method == 'POST':
        if product_wanted.is_valid():
            product_name = product_wanted.cleaned_data['product_name']
            # print(product_name)

            product_from_db = Products.objects.filter(name__iexact=product_name).values()

            if product_from_db:
                # we send it to the page 'results_of_research'
                print(product_from_db[0]) 

                return render(request, 'selected_product.html', product_from_db[0] )

            else:
                """
                If this product is not in the database we have to do something to make the user aware
                """
                print("aucun produit")

        else:
            product_wanted = SearchProductForm()

    return render(request, 'home.html', context)






def selected_product(request, product_to_substitute):
    """
    This view
    """
    name = product_to_substitute['name']
    brand = product_to_substitute['brand']
    store = product_to_substitute['store']
    nutriscore = product_to_substitute['nutriscore']
    fat_lipids_100g = product_to_substitute['fat_lipids_100g']
    saturated_fatty_acids_100g = product_to_substitute['saturated_fatty_acids_100g']
    sugar_100g = product_to_substitute['sugar_100g']
    salt_100g = product_to_substitute['salt_100g']
    photo = product_to_substitute['photo']

    return render(request, 'selected_product.html', name, brand, store, nutriscore, fat_lipids_100g, saturated_fatty_acids_100g, sugar_100g, salt_100g, photo)

def proposed_products(request):
    """
    This view
    """
    return render(request, 'results_of_research.html')

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
