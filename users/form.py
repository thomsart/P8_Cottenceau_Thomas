#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from django.core import validators

from custom_user.models import ClientUser


# Create your models here.

class AccountForm(UserCreationForm):
    class Meta:
        model = ClientUser
        fields = ('first_name', 'email',)

class LoginForm(UserChangeForm):
    class Meta:
        model = ClientUser
        fields = ('email', 'password')

class SearchProductForm(forms.Form):
    product_name = forms.CharField(label='', max_length=70)

class FormNavBar(forms.Form):
    product_name_nav_bar = forms.CharField(label='', max_length=70)
