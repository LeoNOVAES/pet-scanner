#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#coding: utf-8

from Store import Store

class Petz(Store):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.petz.com.br/"
        self.htmlSearch = "search"
        self.htmlListProducts = "liProduct"
        self.htmlNameProduct = "nome_produto"
        self.htmlPriceProduct = "new_price"
        self.htmlLink = "petzProduct"
        self.htmlImage = "product-img"

    def _get_url(self, product):
        try:
            return product.find_element_by_class_name(self.htmlLink).find_element_by_id('produto-href').get_attribute('href')
        except:
           print("url not found!")
                        
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
                    # 'brand': self._get_brand(product).text
                })
            except:
                print("element not found!")
        return productsJson