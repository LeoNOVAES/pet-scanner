#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#coding: utf-8
from Store import Store
import time

class Cobasi(Store):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.cobasi.com.br/"
        self.htmlSearch = "fulltext-search-box"
        self.htmlListProducts = "nm-product-item"
        self.htmlNameProduct = "nm-product-name a"
        self.htmlPriceProduct = "nm-price-value"
        self.htmlLink = "nm-product-name a"
        self.htmlImage = "nm-product-img-container img"
        self.htmlBrand = "linx-brand"


    def searchTerm(self, term = 'None'):
        time.sleep(5)
        search = self.driver.find_element_by_class_name(self.htmlSearch)
        search.send_keys(term)
        self.driver.find_element_by_class_name('btn-buscar').click()
        time.sleep(5)    

    def _get_image(self, product):
        try:
            return product.find_element_by_class_name(self.htmlImage).get_attribute('src')
        except:
            print("nao existe essa calsse nesse elemento de imagens")   

    def _get_brand(self, product):
        try:
            brands = product.find_elements_by_class_name(self.htmlBrand)
            return brands[1]
        except:
            print("nao existe essa calsse nesse elemento de imagens")         

    def _get_all_data(self):
        productsJson = []
        products = self._get_list_products()
        
        for product in products:
            try:
                productsJson.append({
                    'name': self._get_title(product).text,
                    'price': self._get_price(product).text,
                    'url': self._get_url(product),
                    'img': self._get_image(product),
                    'brand': self._get_brand(product).text
                })
            except:
                print("element not found!")
        return productsJson