# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:52:24 2020

@author: payal
"""

import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home',methods=(['GET']))
def checkStatus():
    return "YAY!! its working"

@app.route('/add',methods=(['GET']))
def convertLower():
    a= 2
    b = 3
    return "The sum of {} and {}".format(a,b,a+b)
    

app.run(host='localhost',port=8023)

