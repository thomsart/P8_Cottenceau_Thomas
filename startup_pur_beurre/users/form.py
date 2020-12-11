from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
