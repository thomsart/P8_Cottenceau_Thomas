from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_lenght=40)
    brand = models.CharField(max_lenght=40)
    store = models.TextField()
    nutriscore = models.CharField(max_lenght=1)
    fat_lipids_100g = models.CharField(max_lenght=10)
    saturated_fatty_acids_100g = models.CharField(max_lenght=10)
    sugar_100g = models.CharField(max_lenght=10)
    salt_100g = models.CharField(max_lenght=10)
    photo = 


