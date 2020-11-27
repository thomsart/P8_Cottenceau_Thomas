#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

from . import models as mdl

################################################################################

def main():
    """
    We take from Openfoodfact Api a 'category' of food we want and put it in a
    list of values in order to fill the table made for it in our database.
    For that we create a for loop in fonction of the number of pages
    'nb_page' of the product on the Api, and we put all datas in the table
    we want with the argument 'table'.It's allows us to not repet for
    exemple 20 times the same request.
    """

    category = input("Quelle categorie ?\n")
    nb_pages = int(input("Combien de page ?\n"))
    print("Ok c'est parti !")

    for i in range(nb_pages):
        """
        We choose the food we want to put in the database by the argument
        'category' and the number of pages we want with 'nb_pages'. Be carefull
        to not take more than there are pages on the Api.
        """
        url = 'https://fr-en.openfoodfacts.org/category/' + category + '/'
        + str(i) + '.json'
        response = requests.get(url)
        data = response.json()
        key = data.get("products")
        number_of_product = len(key)
        count = 0

        while count < number_of_product:
            """
            Now we do a while loop to browse and catch all the vallues which
            we need for our table.
            """
            try:

                productApi = key[count]
                product = mdl.Products()

                product.cat = category
                product.name = productApi['product_name']
                product.brand = productApi['brands']
                product.store = productApi['stores']
                product.nutriscore = productApi['nutriscore_grade']
                product.fat_lipids_100g = productApi['fat_100g']
                product.saturated_fatty_acids_100g = productApi['saturated-fat_100g']
                product.sugar_100g = productApi['sugars_100g']
                product.salt_100g = productApi['salt_100g']
                product.photo = productApi['image_url']
                
                product_list = [product.cat, product.name, product.brand, product.store,
                product.nutriscore, product.fat_lipids_100g, product.saturated_fatty_acids_100g,
                product.sugar_100g, product.salt_100g]
                print(product_list)

            except Exception:
                """
                We choose to not take product which don't have the headers that we need.
                """
                count += 1
                continue

            count += 1

    return


if __name__ == "__main__":
    main()