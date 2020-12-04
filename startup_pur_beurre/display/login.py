from django.forms import ModelForm

from database.models import Users

# Create your models here.

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['e_mail', 'password']
    
class AccountForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'e_mail', 'password']