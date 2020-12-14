from django import forms
from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm

from .models import ClientUser


# Create your models here.

class AccountForm(UserCreationForm):

    class Meta:
        model = ClientUser
        fields = ('username','first_name', 'last_name', 'email', 'password')

class LoginForm(UserChangeForm):

    class Meta:
        model = ClientUser
        fields = ('email', 'password')

class SearchProductForm(forms.Form):

    product_name = forms.CharField(label='', max_length=70)

    pass


class SearchForm(forms.Form):

    search = forms.CharField(label='aucune idée', max_length=100)

    pass