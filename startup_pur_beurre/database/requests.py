#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

from . import models

################################################################################

def main():
    """
    We take from Openfoodfact Api a category of 'food' we want and put it in a
    list of values in order to fill the table made for it in our database.
    For that we create a for loop in fonction of the number of pages
    'nb_page' of the product on the Api, and we put all datas in the table
    we want with the argument 'table'.It's allows us to not repet for
    exemple 20 times the same request.
    """

    category = input("Quelle categorie ?\n")
    nb_pages = int(input("Combien de page ?\n"))
    print("Ok")

    self.cursor.execute("""INSERT INTO category (name) VALUE('"""
                        + str(category) + """') """)

    self.cursor.execute("""SELECT id FROM category WHERE name = '"""
                        + str(category) + """' """)


    for i in range(nb_pages):

        """ We choose the food we want to put in the database by the argument
        'food' and the number of pages we want with 'nb_pages'. Be carefull
        to not take more than there are pages on the Api. """

        url = 'https://fr-en.openfoodfacts.org/category/' + category + '/'
        + str(i) + '.json'
        response = requests.get(url)
        data = response.json()
        key = data.get("products")
        number_of_product = len(key)
        count = 0

        """ Now we do a while loop to browse and catch all the vallues which
        we need for our table. """

        while count < number_of_product:

            try:
                product = key[count]
                name = product['product_name']
                brand = product['brands']
                store = product['stores']
                country = product['countries']
                quantity = product['quantity']
                nutriscore = product['nutriscore_grade']
                url = product['url']
                category = str(category)
                product_list = [name, brand, store, country, quantity,
                                nutriscore, url, category]
                print(product_list)

                """ We choose to not take product which don't have the
                headers that we need. """

            except KeyError:
                count += 1
                continue

            count += 1

            """ Now the idea is to put the product_list into the table we
            choose. """

            self.cursor.execute("""INSERT INTO product(name, brand, store,
                country, quantity,nutriscore, url, category)
                VALUE(%s, %s, %s, %s, %s, %s, %s, %s)""", product_list)

    self.cursor.execute("""SELECT id FROM product WHERE category =
                        '"""+str(food)+"""' """)

    the_ids = self.cursor.fetchall()

    for el in the_ids:
        self.cursor.execute("""INSERT INTO product_category (id_product,
                            id_category) VALUES('"""+str(el[0])+"""',
                            '"""+str(id_cat)+"""')""")

    return


if __name__ == "__main__":
    main()