# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:42:38 2022

@author: Professor
"""
def total_trainWords(training):
    
    total_words=[] #total words per email

    # Emails
    for id_number in training: #loop that iterates over each email
    
        #First we count total number of words in emails and sum them up
        total_words.append(len(training[id_number]))
        
    return total_words

def wordTest_in_wordTrain(training, words_test):
    
    #below are parameters required to calculate probabilities of words
    word_count={k:[] for k in words_test}
    
    total_words=total_trainWords(training)
    
    unique_words=[] #unique words in emails
    
    
    # (1) emails
    
    for id_number in training: #loop that iterates over each email
    
        #First we count total number of words in emails and sum them up
        total_words.append(len(training[id_number]))
       
        #Now we compute frequency of words in emails
        word_value={}
        existing= training[id_number]
        for term in existing: 
            if term not in word_value:
                word_value[term]= existing.count(term)
                
        
        words=[]
        for element in word_value:
            
            words.append(element)
        
        #loop for repetitive of each word that occurs in individual email
        occurances={}
        
        for word_test in words_test: #N.B be mindful of 's' words and word test
            for word in words:
                if word_test == word:
                    occurances[word_test]= word_value[word_test]
    
                elif word_test not in words :
                    occurances[word_test]= 0
        
        #loop for repetitive of each word that occurs in all emails
        for word in occurances:
            word_count[word].append(occurances[word])
            
        #loop for unique words in emails
        for unique in training[id_number]:
            if unique not in unique_words:
                unique_words.append(unique) 
    
    return word_count




def unique_words(training):
    unique_words=[] #unique words in emails
    
    # (1) for emails
    for id_number in training: #loop that iterates over each SPAM email
    
    #loop for unique words in emails
        for unique in training[id_number]:
            if unique not in unique_words:
                unique_words.append(unique)
    
    return unique_words

