import pytest
import json

from django.test import TestCase

from database.models import Products
from database.scripts import tools


# Create your tests here

class TestViews(TestCase):

    def  setUp(self):
        """
            We defined here all the datas we need to do the tests.
        """

        # self.product_without_all_fields():{

        # }

        # self.product_with_all_fields():{

        # }

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
        assert tools.is_product_in_file(self.dict_without_product) == False
        assert tools.is_product_in_file(self.dict_with_product) == True

    def test_put_products_in_db(self):
        assert tools.put_products_in_db(self.dict_without_product) == False
        assert tools.put_products_in_db(self.dict_with_product) == True
        assert tools.put_products_in_db(self.dict_with_product_which_miss_one_header) == False
        assert tools.put_products_in_db(self.dict_with_product_which_miss_one_field) == False