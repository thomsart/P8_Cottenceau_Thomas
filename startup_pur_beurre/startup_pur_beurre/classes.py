#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

################################################################################

class Request:
    """
    This class of methods will allows us to do all the requests and treatments
    on the json we get from the Open Food Facts API.
    """

    @staticmethod
    def search_food(food):
        """
        This method will just request Open Food Facts to get all the features
        we need of a specific food like it's photo or nutriscore for exemple. 
        """

        food_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + str(food) + "&format=json"
        json_result = requests.get(food_url)
        json_result = json_result.json()

        return print(json_result)