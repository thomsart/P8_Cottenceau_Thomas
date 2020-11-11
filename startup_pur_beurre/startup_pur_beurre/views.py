from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def results_of_research(request):
    return render(request, 'pages/results_of_research.html')

def saved_products(request):
    return render(request, 'pages/saved_products.html')

def selected_product(request):
    return render(request, 'pages/selected_product.html')

def user_account(request):
    return render(request, 'pages/user_account.html')