#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#coding: utf-8
from Store import Store
import time

class ClubeExtra(Store):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.clubeextra.com.br/"
        self.htmlSearch = "input-form-search input"
        self.htmlListProducts = "ng-isolate-scope"
        self.htmlNameProduct = "product-name"
        self.htmlPriceProduct = "catalog-list-price"
        self.htmlLink = "catalog-info-product a"
        self.htmlImage = "catalog-list-image img"
        self.htmlBrand = "catalog-list-brand"
    
    def searchTerm(self, term = 'None'):
        search = self.driver.find_element_by_class_name(self.htmlSearch)
        search.send_keys(term)
        self.driver.find_element_by_class_name("input-form-search button").click()
        time.sleep(5)

    def _get_all_data(self):
        productsJson = []
        products = self._get_list_products()
        for product in products:
            try:
                productsJson.append({
                    'name': self._get_title(product).text,
                    # 'price': self._get_price(product).text,
                    # 'url': self._get_url(product),
                    # 'img': self._get_image(product),
                    # 'brand': self._get_brand(product).text
                })
            except:
                print("element not found!")
        return productsJson    