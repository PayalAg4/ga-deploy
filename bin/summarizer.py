# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yaml
import numpy as np
from preprocessor import PreprocessDoc

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r')as fl:
            self.config = yaml.load (fl)
        
    def loadDocs(self,filePath):
        with open(filePath,'r',encoding='utf-8') as fl:
            text = fl.read()
        return text
    
    def splitSentences(self,text):
        """
        Split paragraph into array of sentences
        
        Input:
            text: string
        Output:
            sentences: a list of string
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentence(self,sentences):
        """
        Split the sentences into first sentences and rest of the sentences
        
        Input:
            sentences: a list of string
        Output:
            firstSent: string
            restOfSent: a list of string
        """
        firstSent, restOfSent = sentences[0],sentences[1:]
        return firstSent, restOfSent
    
    def findSentLength(self,text):
        """
        Find the length of the sentences
        
        Input:
            text: a list of string
        Output:
            
        """
        return text.split()
            
    def findSentLengthArray(self,sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopSentences(self,sentLengths,sentences,n):
        sortedIdx = np.argsort(sentLengths)
        topnIdx = sortedIdx[-n:]
        topnSentences = [sentences[i] for i in topnIdx]
        return topnSentences
    
    def findSummary(self):
        filePath = self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        sentences = self.splitSentences(text)
        firstSent,restOfSent = self.groupSentence(sentences)
        sentLengths = self.findSentLengthArray(restOfSent)
        topSentences = self.findTopSentences(sentLengths,restOfSent,self.config['sentences_num'])
        allSentences = [firstSent] + topSentences
        summary = ' '.join(allSentences)
        return summary
    
    def preprocess(self,text):
        preprocessObj = PreprocessDoc()
        filteredText = preprocessObj.removeSpclChar(text)
        filteredText = preprocessObj.convertToLower(filteredText)
        return filteredText
        
summarizeObj = SummarizeDoc()
summary = summarizeObj.findSummary()







