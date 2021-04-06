#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

""" In this file we do one functional-test in the 'users' application. """

################################################################################
##                                   TESTS                                    ##
################################################################################

class TestViews(StaticLiveServerTestCase):
    """ We create this test class with the 'StaticLiveServerTestCase' of Django 
    in order to automatise this functionnal test of our plateforme. """

    @classmethod
    def setUpClass(cls):
        """ All the features of our driver like the path to run it. """
       
        super().setUpClass()
        cls.selenium = WebDriver(executable_path="/~/Chromedriver_linux64.exe")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        """ The attribute to close our driver. """

        cls.selenium.quit()
        super().tearDownClass()

    def test_is_product_show(self):
        """ This test allows us to check if the fact that enter in the home-page
        formulaire the 'frosties' product redirect to the 'selected_products/'
        url by checking if the 'selected_products.html' template is used. """

        self.selenium.get("http://localhost:8000/")
        response = self.selenium.find_element(By.ID, "id_product_name")
        response.send_keys("frosties")
        response.send_keys(Keys.ENTER)
        self.assertTemplateUsed('selected_product.html')

################################################################################
