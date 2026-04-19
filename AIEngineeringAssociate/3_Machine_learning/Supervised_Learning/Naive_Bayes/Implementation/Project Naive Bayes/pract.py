# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:43:51 2022

@author: Professor
"""
import nltk
import math

t= 'Hello good people, I am extending My greetings HELLA!'


#nltk.download('words')
words= set(nltk.corpus.words.words())


k={'hello': [3,6,9], 'bye':[2,4,6]}

prod= [1,2,3,4,5,6,7]


product =1
for i in prod:
    product=product*i
    
    
print(product)