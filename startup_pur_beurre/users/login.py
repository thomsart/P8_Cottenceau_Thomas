from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from database.models import ClientUser


# Create your models here.

class AccountForm(UserCreationForm):

    class Meta:
        model = ClientUser
        fields = ('__all__')

class LoginForm(UserChangeForm):

    class Meta:
        model = ClientUser
        fields = ('email', 'password')
