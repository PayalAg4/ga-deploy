# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 02:01:13 2020

@author: payal
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary
    

app.run(host='localhost',port=8023)

