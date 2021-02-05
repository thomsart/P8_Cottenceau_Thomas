import pytest
import json

@pytest.fixture
def product_without_all_fields():
    return

@pytest.fixture
def product_with_all_fields():
    return

@pytest.fixture
def dict_without_product():
    return {
        "category": "category",
        "number_of_products": 0,
        "list_of_products": []
    }

@pytest.fixture
def dict_with_product():
    return {
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

@pytest.fixture
def dict_with_product_which_miss_one_header():
    return {
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

@pytest.fixture
def dict_with_product_which_miss_one_field():
    return {
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