#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from ..models import Products
from ..json_folder import *

################################################################################

"""
    This module contains all the methods used to create new 'Product' model in
    the database. From the opening of the json file to the saving of the products
    in the database.
"""

################################################################################

def open_json_file(name_file):

    """
        This method open a json and put all the datas we need in a dictionary.
    """
    category = name_file.split('_')
    number_of_product = 0
    list_of_products = []

    try:
        with open("database/json_folder/" + name_file + "", encoding='utf-8') as js:

            data = json.load(js)
            key = data.get("products")
            number_of_product += len(key)
            list_of_products.append(key)

    except Exception:
        print("Aucun fichier '" + name_file + "' n'éxiste dans ce repertoire.")

        return False

    return {
        'category': category[0],
        'number_of_products': number_of_product,
        'list_of_products': list_of_products
    }

################################################################################

def is_product_in_file(dict):

    """
        This methode just check if at least one product exist in the dictionary
        and return 'True' when it's the case if not 'False'. 
    """
    if dict['number_of_products'] == 0:
        print("Aucun produit n'est présent dans ce fichier.")
        return False

    else:
        return True

################################################################################

def put_products_in_db(dict):

    """
        This method extracts from the dict the products from the dictionary
        and return 'True' when at least one product was saved in db and 'False'
        if it's not the case. 
    """
    new_product_in_db = 0
    count = 0
    while count < dict['number_of_products']:
        """
        Now we do a while loop to browse and catch all the values which
        we need for our table 'products'.
        """
        try:
            productApi = dict['list_of_products'][0][count]
            product = Products()
            product.cat = dict['category']
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
            product.save()
            new_product_in_db += 1

        except Exception:
            """
            We choose to not take products for which the headers are empty or missed.
            """
            count += 1
            continue

        count += 1

    if new_product_in_db > 0:
        print(str(new_product_in_db) + " produit(s) vient(nent) d'être ajouté(s) dans la base.")
        return True
    
    else:
        print("Aucun produit n'a été ajouté dans la base.")
        return False

################################################################################