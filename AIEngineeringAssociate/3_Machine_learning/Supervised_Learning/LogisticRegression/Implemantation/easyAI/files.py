# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:47:22 2022

@author: Professor
"""
import glob
import os

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import string

def open_txt(file_path):
    
    stop_words=set(stopwords.words('english'))  #unuseful words like, the, is in etc
    
    english_words= set(nltk.corpus.words.words())  #English words
    
    #Below is a data structures containing data set
    data={}
    
    #(a) Opening spam files, cleaning it and presenting them as a dictionary
    
    #(a.1) opening spam datasets
    x=1
    for filename in glob.glob(os.path.join(file_path, '*.txt')):
      
        with open(filename, 'r', encoding='ISO-8859-1' ) as infile:
            
            tokenized_email= []
            punctuated_email= infile.read()
            
            #below we remove punctuations
            
            unpuctuated_email= punctuated_email.translate(str.maketrans('','',string.punctuation))
            
            #We lower all upper cases since stop words is case sensitive
            lowered_unpactuated= unpuctuated_email.lower()
            
            #considering only English words
            eng_words=[]
            for word in word_tokenize(lowered_unpactuated):
                if word in  english_words:
                    eng_words.append(word)
            
            #removing stop words e.g the, I, in etc
            for word in eng_words:
                if word not in stop_words:
                    
                    #below we stem words e.g running to run
                    stemmed_word= PorterStemmer().stem(word)
                    
                    tokenized_email.append(stemmed_word)
           
        #Here we update the  ids (to use it in a dictionary)
        id_count= 'id' + str(x)
        x=x+1
        
        data[id_count]= tokenized_email
        
    
        
    
        return print(tokenized_email)
    
