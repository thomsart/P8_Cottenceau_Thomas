#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.last_name

class Products(models.Model):
    cat = models.CharField(max_length=20)
    name = models.TextField()
    brand = models.TextField()
    store = models.TextField()
    nutriscore = models.CharField(max_length=1)
    fat_lipids_100g = models.CharField(max_length=10)
    saturated_fatty_acids_100g = models.CharField(max_length=10)
    sugar_100g = models.CharField(max_length=10)
    salt_100g = models.CharField(max_length=10)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class SavedProducts(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Products, models.SET_NULL, null=True)
