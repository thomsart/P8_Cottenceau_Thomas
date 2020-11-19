#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def results_of_research(request):
    return render(request, 'pages/results_of_research.html')

def saved_products(request):
    return render(request, 'pages/saved_products.html')

def selected_product(request):
    return render(request, 'pages/selected_product.html')

def user_account(request):
    return render(request, 'pages/user_account.html')

def mentions_legales(request):
    return render(request, 'pages/mentions_legales.html')

def error_404(request):
    return render(request, 'errors/error_404.html')

def error_500(request):
    return render(request, 'errors/error_500.html')
