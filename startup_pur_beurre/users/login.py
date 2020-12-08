from django.forms import ModelForm

from database.models import Users

# Create your models here.

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            'e_mail',
            'password'
            ]

class AccountForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'