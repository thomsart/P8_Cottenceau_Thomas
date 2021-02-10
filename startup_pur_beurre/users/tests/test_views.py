#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse
from database.models import Products
from users.models import ClientUser
from django.contrib import messages



# Create your tests here.

################################################################################

class TestViews(TestCase):

    def setUp(self):
        """
            We defined here all the datas we need to do the tests.
        """

        self.client = Client()

        self.user = ClientUser.objects.create(
            password='hidao1985+',
            username='Dédé',
            first_name='Dédé',
            last_name='Patel',
            email='theemail@gmail.com',
            )

        self.product = Products.objects.create(
            cat= 'test',
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
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_search_product(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('selected_product/', args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'selected_product.html')

    def test_search_product_failed(self):
        response = self.client.get(reverse('search_product/'))
        self.assertEqual(response.status_code, 302)
    
    def test_selected_product(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('selected_product/', args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'selected_product.html')
    
    def test_proposed_products(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('proposed_products/', args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposed_products.html')

    def test_mentions_legales(self):
        response = self.client.get(reverse('mentions_legales/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')  

    def test_signup(self):

    def test_login(self):

    def test_save_product(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('save_product/', args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposed_products.html')

    def test_user_substitutes(self):
        response = self.client.get(reverse('user_substitutes/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_substitutes.html')

    def test_delete_product(self):
        response = self.client.get(reverse('delete_product/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_substitutes.html')

    def test_account(self):
        response = self.client.get(reverse('account/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
