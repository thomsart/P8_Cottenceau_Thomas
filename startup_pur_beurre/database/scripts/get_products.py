#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

from ..models import Products
from ..json_folder import *

################################################################################

def run():
    """
    
    """
    # category = input("Quelle categorie ?\n")
    # nb_pages = input("Combien de page ?\n")
    # nb_pages = int(nb_pages)
    # print("Ok c'est parti !")

    # for i in range(nb_pages):
    #     """
    #     We choose the food we want to put in the database by the argument
    #     'category' and the number of pages we want with 'nb_pages'. Be carefull
    #     to not take more than there are pages on the Api.
    #     """
    #     url = 'https://fr-en.openfoodfacts.org/category/' + category + '/' + str(i + 1) + '.json'
    #     response = requests.get(url)
    #     data = response.json()

    name_file = input("quel json veux tu traiter ?")

    with open("database/json_folder/"+name_file+"", encoding='utf-8') as js:

        data = json.load(js)
        data
        key = data.get("products")
        number_of_product = len(key)
        count = 0

        while count < number_of_product:
            """
            Now we do a while loop to browse and catch all the values which
            we need for our table 'products'.
            """
            try:
                productApi = key[count]
                product = Products()

                product.cat = "spaghetti"
                product.name = productApi['product_name']
                product.brand = productApi['brands']
                product.store = productApi['stores']
                product.nutriscore = productApi['nutriscore_grade']
                product.fat_lipids_100g = productApi['nutriments']['fat_100g']
                product.saturated_fatty_acids_100g = productApi['nutriments']['saturated-fat_100g']
                product.sugar_100g = productApi['nutriments']['sugars_100g']
                product.salt_100g = productApi['nutriments']['salt_100g']
                product.photo = productApi['image_url']
                product.link = productApi['url']

                # print(category)
                # print(productApi['product_name'])
                # print(productApi['brands'])
                # print(productApi['stores'])
                # print(productApi['nutriscore_grade'])
                # print(productApi['nutriments']['fat_100g'])
                # print(productApi['nutriments']['saturated-fat_100g'])
                # print(productApi['nutriments']['sugars_100g'])
                # print(productApi['nutriments']['salt_100g'])
                # print(productApi['image_url'])

                product_list = [product.cat, product.name, product.brand, product.store,
                product.nutriscore, product.fat_lipids_100g, product.saturated_fatty_acids_100g,
                product.sugar_100g, product.salt_100g, product.photo]
                print(product_list)
                print("\n\n\n")

                product.save()

            except Exception:
                """
                We choose to not take products for which the headers are empty or missed.
                """
                print("----------\n")
                count += 1
                continue

            count += 1

    return print("Terminé.")
