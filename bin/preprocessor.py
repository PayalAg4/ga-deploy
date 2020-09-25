# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Given an array, find the mean of that array without using numpy
import re

class PreprocessDoc:
    """
    Module for preprocessing articles
    """
    
    def removeSpclChar(self,text):
        """
        Remove special Characters
        
        Input:
            text: string
        Output:
            modifiedText: string
        """
        filteredText = re.sub(',|;|#|$','',text)
        return filteredText
    
    def convertToLower(self,text):
        return text.lower()
    

    
   