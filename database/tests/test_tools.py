#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import json

from django.test import TestCase

from database.models import Products
from database.management.commands import _tools as tools

""" Here are all our tools-tests which allows us to fill our database with json
files we dowloaded from 'Open Food facts API'. """

################################################################################
##                                  TESTS                                     ##
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """ We defined here all the datas we need to do our tests. """

        self.dict_without_product = {
                "category": "category",
                "number_of_products": 0,
                "list_of_products": []
            }

        self.dict_with_product = {
                "category": "test",
                "number_of_products": 1,
                "list_of_products": [[
                    {"product_name": "tube_head_667",
                    "brands": "randall",
                    "particularity": "it's_makes_me_happy_when_I_plug_it_and_play",
                    "stores": "carrouf",
                    "nutriscore_grade": "a",
                    "nutriments": {
                        "fat_100g": 0.5,
                        "saturated-fat_100g": 0.5,
                        "sugars_100g": 0.5,
                        "salt_100g": 0.5
                        },
                    "image_url": "https://static.openfoodfacts.org/images/products/261/front_fr.jpg",
                    "url": "https://en-fr.openfoodfacts.org/the_url_of_the_product.com",
                    "an_other_header": "lets_imagine_an_other_header_to_check_"
                    }
                ]]
            }

        self.dict_with_product_which_miss_one_header = {
                "category": "test",
                "number_of_products": 1,
                "list_of_products": [[
                    {"product_name": "tube_head_667",
                    "brands": "randall",
                    "particularity": "it's_makes_me_happy_when_I_plug_it_and_play",
                    "stores": "carrouf",
                    "nutriscore_grade": "a",
                    "nutriments": {
                        "saturated-fat_100g": 0.5,
                        "sugars_100g": 0.5,
                        "salt_100g": 0.5
                        },
                    "image_url": "https://static.openfoodfacts.org/images/products/261/front_fr.jpg",
                    "url": "https://en-fr.openfoodfacts.org/the_url_of_the_product.com",
                    "an_other_header": "lets_imagine_an_other_header_to_check_"
                    }
                ]]
            }

        self.dict_with_product_which_miss_one_field = {
                "category": "test",
                "number_of_products": 1,
                "list_of_products": [[
                    {"product_name": "tube_head_667",
                    "brands": "randall",
                    "particularity": "it's_makes_me_happy_when_I_plug_it_and_play",
                    "stores": "carrouf",
                    "nutriscore_grade": "a",
                    "nutriments": {
                        "fat_100g": 0.5,
                        "saturated-fat_100g": 0.5,
                        "sugars_100g": 0.5,
                        "salt_100g": 0.5
                        },
                    "image_url": None,
                    "url": "https://en-fr.openfoodfacts.org/the_url_of_the_product.com",
                    "an_other_header": "lets_imagine_an_other_header_to_check_"
                    }
                ]]
            }


    def test_is_product_in_file(self):
        """ Here we make sure that there's at least one good product that matchs
        with our model fields in returning 'True'. In the wrong case it return
        'False' we can delete this file. """

        assert tools.is_product_in_file(self.dict_without_product) == False
        assert tools.is_product_in_file(self.dict_with_product) == True

    def test_put_products_in_db(self):
        """ Here we make sure that this function put in the database a product
        when it matches with our expectations and doesn't put it when it's
        not the case. """

        assert tools.put_products_in_db(self.dict_without_product) == False
        assert tools.put_products_in_db(self.dict_with_product) == True
        assert tools.put_products_in_db(
            self.dict_with_product_which_miss_one_header) == False
        assert tools.put_products_in_db(
            self.dict_with_product_which_miss_one_field) == False

################################################################################
