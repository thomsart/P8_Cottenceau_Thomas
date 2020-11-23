from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)

class Products(models.Model):
    cat = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    store = models.TextField()
    nutriscore = models.CharField(max_length=1)
    fat_lipids_100g = models.CharField(max_length=10)
    saturated_fatty_acids_100g = models.CharField(max_length=10)
    sugar_100g = models.CharField(max_length=10)
    salt_100g = models.CharField(max_length=10)
    photo = models.ImageField()

class SavedProducts(models.Model):
    user = models.ManyToManyField(Users, verbose_name="User ID")
    product = models.ManyToManyField(Products, verbose_name="Product ID")
