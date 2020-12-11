#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ClientUser(AbstractUser):
    pass

    def __str__(self):
        return self.username