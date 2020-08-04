#coding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#coding: utf-8

from flask import Flask
from flask import jsonify
from flask import request

from PetLove import PetLove
from Petz import Petz
from ClubeExtra import ClubeExtra
from Cobasi import Cobasi
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import time

app = Flask(__name__)

option = Options()
ff = webdriver.Firefox(options=option)

@app.route("/api/pet-love")
def getPetLove():
    pet_love = PetLove(ff)
    pet_love.navigate()
    pet_love.searchTerm(request.args.get('term'))
    body_pet_love = pet_love._get_all_data()
    return jsonify(body_pet_love)

@app.route("/api/petz")
def getPetz():
    petz = Petz(ff)
    petz.navigate()
    petz.searchTerm(request.args.get('term'))
    body_petz = petz._get_all_data()
    return jsonify(body_petz)

@app.route("/api/clube-extra")
def getClubeExtra():
    clube_extra = ClubeExtra(ff)
    clube_extra.navigate()
    clube_extra.searchTerm(request.args.get('term'))
    body_clube_extra = clube_extra._get_all_data()
    return jsonify(body_clube_extra)       

@app.route("/api/cobasi")
def getCobasi():
    cobasi = Cobasi(ff)
    cobasi.navigate()
    cobasi.searchTerm(request.args.get('term'))
    body_cobasi = cobasi._get_all_data()
    return jsonify(body_cobasi)       


if __name__ == "__main__":
    app.run()