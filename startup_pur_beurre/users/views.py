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

            if product:
                product_id = product[0]['id']
                print(product_id)
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

    cat = product['category']
    name = product['name']
    brand = product['brand']
    store = product['store']
    nutriscore = product['nutriscore']
    fat_lipids_100g = product['fat_lipids_100g']
    saturated_fatty_acids_100g = product['saturated_fatty_acids_100g']
    sugar_100g = product['sugar_100g']
    salt_100g = product['salt_100g']
    photo = product['photo']

    substitute_form = SubstituteForm(request.GET)
    context = {'substitute_form': substitute_form}

    if request.method == 'GET':
        if substitute_form.is_valid():
            print("OK")
            return redirect('proposed_products/', cat, nutriscore)
        else:
            substitute_form = SubstituteForm()

    return render(request, 'selected_product.html', context, name, brand, store, nutriscore, fat_lipids_100g, saturated_fatty_acids_100g, sugar_100g, salt_100g, photo)



















def proposed_products(request, cat, nutriscore):
    """
    This view
    """



    return render(request, 'proposed_products.html')







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
