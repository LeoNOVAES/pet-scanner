from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import json
import time

class Store:

    def navigate(self):
        self.driver.get(self.url)

    def searchTerm(self, term = 'None'):
        search = self.driver.find_element_by_id(self.htmlSearch)
        search.send_keys(term)
        search.send_keys(Keys.ENTER)
        time.sleep(5)

    def _get_list_products(self):
        return self.driver.find_elements_by_class_name(self.htmlListProducts)

    def _get_title(self, product):
        try:
            return product.find_element_by_class_name(self.htmlNameProduct)
        except:
            print("titles not found")

    def _get_price(self, product):
        try:
            return product.find_element_by_class_name(self.htmlPriceProduct)
        except:
            print("price not found!")

    def _get_brand(self, product):
        try:
            return product.find_element_by_class_name(self.htmlBrand)
        except:
            print("nao existe essa calsse nesse elemento de imagens")

    def _get_url(self, product):
        try:
            return product.find_element_by_class_name(self.htmlLink).get_attribute('href')
        except:
           print("url not found!")                 

    def _get_image(self, product):
        try:
            return product.find_element_by_class_name(self.htmlImage).get_attribute('data-src')
        except:
            print("nao existe essa calsse nesse elemento de imagens")
    
    
        
                                      