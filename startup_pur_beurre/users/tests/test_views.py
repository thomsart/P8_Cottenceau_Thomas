#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse
from users.models import *


# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_search_product(self):
        response = self.client.get(reverse('search_product/'))
        self.assertEquals(response.status_code, 200)



















# @pytest.mark.parametrize('param', [
#     'home',
#     'signup',
#     'mentions_legales/'
# ])
# def test_render_views(client, param):
#     temp_url = urls.reverse(param)
#     response = client.get(temp_url)
#     assert response.status_code == 200

# def test_render_account(client):
#     temp_url = urls.reverse('account/')
#     response = client.get(temp_url)
#     assert response.status_code == 302







# @pytest.mark.django_db
# def test_signup(client, user_data):
#     user_model = get_user_model()
#     assert user_model.objects.count() == 0
#     signup_url = urls.reverse('signup')
#     response = client.post(signup_url, user_data)
#     assert user_model.objects.count() == 1
#     assert response.status_code == 302
