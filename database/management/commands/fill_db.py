#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from urllib3.exceptions import InsecureRequestWarning

from . import _tools as tools

import urllib3
import logging
import ssl
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter


""" This command was creates to put all products that we download in json format
from the API Openfoodfact. The idea is to take only complete product.
The only field we decide to permit a blank is for the "store", because
first a lot of product in this API doesn't have this features and secondly
it doesn't avoid a client to refer to it as long as he have it's name and
brand and nutritional composition. """

################################################################################



class Command(BaseCommand):

    help = "Fill the database with requesting the Open Food Facts API."

    def handle(self, *args, **options):

        category = input("Quelle categorie veux-tu importer ?\n")
        num_of_page = input("A partir de qu'elle page veux tu commencer ?\n")

        while num_of_page != 0:
            json = tools.search_json_file(category, num_of_page)

            if json == False:
                num_of_page == 0

                return print("End !")

            else:
                num_of_page += 1
                
                if tools.is_product_in_file(json) == True:
                    tools.put_products_in_db(json)

                else:
                    pass