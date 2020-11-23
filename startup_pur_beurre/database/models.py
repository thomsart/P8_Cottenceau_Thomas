from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    sex = models.CharField(max_length=1)
    e_mail = models.EmailField()

class SavedProducts(models.Model):
    id_user = models.PositiveIntegerField()
    cat = models.CharField(max_length=20)
    id_product = models.PositiveIntegerField()
    

class CornFlakes(models.Model):

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

class Spaghetti(models.Model):

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

class Riz(models.Model):

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

class PatteTartiner(models.Model):

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


