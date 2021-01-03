"""startup_pur_beurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account/', views.account),
    path('selected_product/<product_id>/', views.selected_product, name='selected_product/'),
    path('selected_product/<product_id>/proposed_products/', views.proposed_products, name='proposed_products/'),
    path('saved_products/', views.saved_products),
    path('mentions_legales/', views.mentions_legales),
    path('index/', views.index, name="index"),
]
