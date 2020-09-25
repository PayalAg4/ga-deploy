# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:52:24 2020

@author: payal
"""

import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def checkStatus():
    return "YAY!! its working!"

@app.route('/add',methods=['GET'])
def addNum():
    a = 2
    b = 6
    return " The sum of {} & {} is {} ".format(a,b,a+b)
    

app.run(host='localhost',port=1123)


