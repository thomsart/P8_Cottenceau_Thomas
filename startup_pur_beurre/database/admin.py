from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.login import AccountForm, LoginForm
from .models import ClientUser

class ClientUserAdmin(UserAdmin):
    add_form = AccountForm
    form = LoginForm
    model = ClientUser
    list_display = ['username', 'email']

admin.site.register(ClientUser, ClientUserAdmin)