from django.db import models

# Create your models here.

class User(models.Model):
    id = models.PositiveIntegerField()
    first_name = models.CharField(max_lenght=40)
    last_name = models.CharField(max_lenght=40)
    sex = models.CharField(max_lenght=1)
    e_mail = models.EmailField()

class SavedProducts(models.Model):
    id_user = models.PositiveIntegerField()
    id_product = models.PositiveIntegerField()
    cat = models.CharField(max_lenght=20)

class Cornflakes(models.Model):
    id = models.PositiveIntegerField()
    cat = models.CharField(max_lenght=20)
    name = models.CharField(max_lenght=40)
    brand = models.CharField(max_lenght=40)
    store = models.TextField()
    nutriscore = models.CharField(max_lenght=1)
    fat_lipids_100g = models.CharField(max_lenght=10)
    saturated_fatty_acids_100g = models.CharField(max_lenght=10)
    sugar_100g = models.CharField(max_lenght=10)
    salt_100g = models.CharField(max_lenght=10)
    photo = models.ImageField()

class Spaghetti(models.Model):
    id = models.PositiveIntegerField()
    cat = models.CharField(max_lenght=20)
    name = models.CharField(max_lenght=40)
    brand = models.CharField(max_lenght=40)
    store = models.TextField()
    nutriscore = models.CharField(max_lenght=1)
    fat_lipids_100g = models.CharField(max_lenght=10)
    saturated_fatty_acids_100g = models.CharField(max_lenght=10)
    sugar_100g = models.CharField(max_lenght=10)
    salt_100g = models.CharField(max_lenght=10)
    photo = models.ImageField()

class Riz(models.Model):
    id = models.PositiveIntegerField()
    cat = models.CharField(max_lenght=20)
    name = models.CharField(max_lenght=40)
    brand = models.CharField(max_lenght=40)
    store = models.TextField()
    nutriscore = models.CharField(max_lenght=1)
    fat_lipids_100g = models.CharField(max_lenght=10)
    saturated_fatty_acids_100g = models.CharField(max_lenght=10)
    sugar_100g = models.CharField(max_lenght=10)
    salt_100g = models.CharField(max_lenght=10)
    photo = models.ImageField()

class PatteTartiner(models.Model):
    id = models.PositiveIntegerField()
    cat = models.CharField(max_lenght=20)
    name = models.CharField(max_lenght=40)
    brand = models.CharField(max_lenght=40)
    store = models.TextField()
    nutriscore = models.CharField(max_lenght=1)
    fat_lipids_100g = models.CharField(max_lenght=10)
    saturated_fatty_acids_100g = models.CharField(max_lenght=10)
    sugar_100g = models.CharField(max_lenght=10)
    salt_100g = models.CharField(max_lenght=10)
    photo = models.ImageField()


