#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse
from database.models import Products
from users.models import ClientUser



# Create your tests here.

################################################################################

class TestViews(TestCase):

    def setUp(self):
        """
            We defined here all the datas we create to simulate the tests.
        """

        self.client = Client()

        self.user = ClientUser.objects.create(
            id=999,
            password='hidao1985+',
            is_superuser=False,
            username='Dédé',
            first_name='Dédé',
            last_name='Patel',
            email='theemail@gmail.com',
            is_active=True
            )

        self.product = Products.objects.create(
            id=999997,
            cat='test',
            name='product',
            brand='brand',
            store='store',
            nutriscore='b',
            fat_lipids_100g='0.5',
            saturated_fatty_acids_100g='0.5',
            sugar_100g='0.5',
            salt_100g='0.5',
            photo='https://static.openfoodfacts.org/images/products.jpg',
            link='https://fr-en.openfoodfacts.org/product/comte-12-mois-juraflore'
            )

        self.product_without_substitute = Products.objects.create(
            id=999998,
            cat='test',
            name='product_without_substitute',
            brand='brand',
            store='store',
            nutriscore='a',
            fat_lipids_100g='0.5',
            saturated_fatty_acids_100g='0.5',
            sugar_100g='0.5',
            salt_100g='0.5',
            photo='https://static.openfoodfacts.org/images/products.jpg',
            link='https://fr-en.openfoodfacts.org/product/comte-12-mois-juraflore'
            )

        self.substitute = Products.objects.create(
            id=999999,
            cat='test',
            name='substitute',
            brand='brand',
            store='store',
            nutriscore='a',
            fat_lipids_100g='0.5',
            saturated_fatty_acids_100g='0.5',
            sugar_100g='0.5',
            salt_100g='0.5',
            photo='https://static.openfoodfacts.org/images/products.jpg',
            link='https://fr-en.openfoodfacts.org/product/comte-12-mois-juraflore'
            )

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_search_product(self):
        id_product = Products.objects.filter(name="product").get('id')
        response = self.client.get(reverse('selected_product/', args=id_product))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'selected_product.html')

