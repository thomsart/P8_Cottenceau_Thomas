#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from urllib3.exceptions import InsecureRequestWarning
import requests
from ..models import Products
from . import tools
import urllib3
import logging
import ssl
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

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

    name_file = input("quel json veux tu traiter ?    ")
    file_json = tools.open_json_file(name_file)

    if file_json == False:

        return print("End !")

    else:
        if tools.is_product_in_file(file_json) == True:
            tools.put_products_in_db(file_json)

        else:
            pass

        return print("End !")

################################################################################

    # category = input("Quelle categorie veux tu importer ?\n")
    # url = 'https://fr-en.openfoodfacts.org/category/' + category + '/1.json'
    # response = requests.get(url)
    # data = response.json()
    # key = data.get("products")
    # print(data)
    # print(key)

    # return


    # i = 1
    # try:
    #     url = 'https://fr-en.openfoodfacts.org/category/' + category + '/' + str(i + 1) + '.json'
    #     response = requests.get(url)
    #     data = response.json()
    #     i += 1
    # except