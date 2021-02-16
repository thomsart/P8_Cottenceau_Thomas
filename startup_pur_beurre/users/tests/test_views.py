#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse
from database.models import Products
from users.models import ClientUser
from django.contrib import messages

""" In this file we test all our views in the 'users' application in asserting
of the used templates, the requests code or the urls redirections. """

################################################################################
##                                 TESTS                                      ##
################################################################################

class TestViews(TestCase):

    def setUp(self):
        """ We defined here all the datas we create to do our tests. """

        self.client = Client()

        self.user_signup = {
            'username': 'dédé',
            'first_name': 'dédé',
            'last_name': 'patel',
            'email': 'dedepatel@gmail.com',
            'password1': 'thepassword1985+',
            'password2': 'thepassword1985+',
        }

        self.user_login = ClientUser.objects.create_user(
            password='21virgulegigawatts+',
            username='george',
            first_name='george',
            last_name='mcfly',
            email='backtothefutur@gmail.com',
            is_active=True
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

        self.product_datas = Products.objects.filter(name='product').values()[0]

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

        return super().setUp()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_search_product(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('selected_product/',
                                            args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'selected_product.html')

    def test_search_product_failed(self):
        response = self.client.get(reverse('search_product/'))
        self.assertEqual(response.status_code, 302)

    def test_selected_product(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('selected_product/',
                                            args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'selected_product.html')
    
    def test_proposed_products(self):
        id_product = Products.objects.get(name="product").id
        response = self.client.get(reverse('proposed_products/',
                                            args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposed_products.html')

    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_success(self):
        response = self.client.post(reverse('signup'), self.user_signup,
                                    format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_login_success(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'george',
                                    'password': '21virgulegigawatts+'
                                    })
        self.assertEqual(response.status_code, 302)

    def test_save_product(self):
        self.client.force_login(self.user_login)
        id_product = Products.objects.get(name="product").id
        response = self.client.post(reverse('proposed_products/',
                                            args=[id_product]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposed_products.html')

    def test_user_substitutes(self):
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('user_substitutes/'),
                                    self.product_datas, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_substitutes.html')

    def test_delete_product(self):
        self.client.force_login(self.user_login)
        id_product = Products.objects.get(name="product").id
        response = self.client.post(reverse('delete_product/',
                                            args=[id_product]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user_substitutes/')

    def test_account(self):
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('account/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_mentions_legales(self):
        response = self.client.get(reverse('mentions_legales/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')

################################################################################