from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django_use_email_as_username.admin import BaseUserAdmin

from .form import AccountForm, LoginForm
from custom_user.models import ClientUser

class ClientUserAdmin(BaseUserAdmin):
    add_form = AccountForm
    form = LoginForm
    model = ClientUser
    list_display = ['email', 'password']

admin.site.register(ClientUser, ClientUserAdmin)