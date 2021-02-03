#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from ..models import Products
from . import tools

################################################################################

def run():
    """
        This script was made to put all products that we download in json format
        from the API Openfoodfact. The idea is to take only complete product.
        The only field we decide to permit a blank is for the "store", because
        first a lot of product in this API doesn't have this features and secondly
        it doesn't avoid a client to refer to it as long as he have it's name and
        brand and nutritional composition.
    """

    name_file = input("quel json veux tu traiter ?")
    file_json = tools.open_json_file(name_file)

    count = 0
    while count < file_json['number_of_products']:
        """
        Now we do a while loop to browse and catch all the values which
        we need for our table 'products'.
        """
        try:
            productApi = file_json['list_of_products'][0][count]
            product = Products()

            product.cat = file_json['category']
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

            product_list = [product.cat, product.name, product.brand, product.store,
            product.nutriscore, product.fat_lipids_100g, product.saturated_fatty_acids_100g,
            product.sugar_100g, product.salt_100g, product.photo]
            print(product_list)
            print("\n")

            # product.save()

        except Exception:
            """
            We choose to not take products for which the headers are empty or missed.
            """
            print("==========Incomplete product==========\n")
            count += 1
            continue

        count += 1

    return print("End !")

    # category = input("Quelle categorie veux tu importer ?\n")
    # url = 'https://fr-en.openfoodfacts.org/category/' + category + '/1.json'
    # response = requests.get(url, verify=False)
    # data = response.json()
    # print(data)
    # return  

    # i = 1
    # try:
    #     url = 'https://fr-en.openfoodfacts.org/category/' + category + '/' + str(i + 1) + '.json'
    #     response = requests.get(url)
    #     data = response.json()
    #     i += 1
    # except