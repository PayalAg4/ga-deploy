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
    
    def loadConfig(self):
        pass
    
    def splitSentences(self,text):
        """
        Split paragraph into an
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentence(self,sentences):
        firstSent, restOfSent = sentences[0],sentences[1:]
        return firstSent, restOfSent
    
    def findSentLength(self,text):
        return text.split()
            
    def findsentLengthArray(self,sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopSentences(self,sentLengths,sentences,n):
        sortedIdx = np.argsort(sentLengths)
        top3Idx = sortedIdx[-n:]
        topnSentences = [sentences[i] for i in top3Idx]
        return topnSentences
    
    def findSummary(self):
        filePath = self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        sentences = self.splitSentences(text)
        firstSent,restOfSent = self.groupSentence(sentences)
        sentLengths = self.findsentLengthArray(restOfSent)
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







