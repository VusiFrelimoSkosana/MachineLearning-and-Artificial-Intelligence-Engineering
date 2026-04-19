# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 16:08:59 2022

@author: Professor
"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
#Lemmatization is some sort of synonym to the original word, often you end up with same word
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("beautiful", pos='a'))
print(lemmatizer.lemmatize("cattle", pos="n"))
print(lemmatizer.lemmatize("better", pos='a'))
print(lemmatizer.lemmatize("begin"))