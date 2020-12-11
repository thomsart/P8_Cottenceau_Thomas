#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import ClientUser

# Create your models here.

# class ClientUser(AbstractUser):
#     pass

#     def __str__(self):
#         return self.user_name

class Products(models.Model):
    cat = models.CharField(max_length=20)
    name = models.TextField(null=True)
    brand = models.TextField()
    store = models.TextField(null=True)
    nutriscore = models.CharField(max_length=1)
    fat_lipids_100g = models.CharField(max_length=10)
    saturated_fatty_acids_100g = models.CharField(max_length=10)
    sugar_100g = models.CharField(max_length=10)
    salt_100g = models.CharField(max_length=10)
    photo = models.URLField(max_length=250)

    def __str__(self):
        return self.name

class SavedProducts(models.Model):
    user_id = models.ForeignKey(ClientUser, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Products, models.SET_NULL, null=True)
