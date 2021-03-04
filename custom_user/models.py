from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class ClientUser(BaseUser):
    objects = BaseUserManager()

    def __str__(self):
        return self.first_name
