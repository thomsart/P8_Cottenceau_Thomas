#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from ..models import Products
from ..json_folder import *


def open_json_file(name_file):

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

    return {
        'category': category[0],
        'number_of_products': number_of_product,
        'list_of_products': list_of_products
    }