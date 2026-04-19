# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:04:40 2022

@author: Vusi Skosana
"""
import glob
import os

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import string

from easyAI.vectorize import wordTest_in_wordTrain
from easyAI.vectorize import total_trainWords
from easyAI.vectorize import unique_words
from easyAI.probabilities import laplace_smoothing_propabilities
from easyAI.probabilities import likelihood
from easyAI.probabilities import Naive_Bayes_eq




file_path_spam = 'spam'
file_path_not_spam = 'ham'
file_path_test='test'

stop_words=set(stopwords.words('english'))  #unuseful words like, the, is in etc

english_words= set(nltk.corpus.words.words())  #English words

#Below are data structures containing training and test data set
training_spam={}
training_not_spam={}

test={}

#(a) Opening spam files, cleaning it and presenting them as a dictionary

#(a.1) opening spam datasets
x=1
for filename in glob.glob(os.path.join(file_path_spam, '*.txt')):
  
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
    id_count= 'id'+str(x)
    x=x+1
    
    training_spam[id_count]= tokenized_email

#(b.1) opening non spam datasets
y=1
for filename in glob.glob(os.path.join(file_path_not_spam, '*.txt')):

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
            if word not in stop_words and english_words:
                
                #below we stem words e.g running to run
                stemmed_word= PorterStemmer().stem(word)
                
                tokenized_email.append(word)
       
    #Here we update the  ids (to use it in a dictionary)
    id_count= 'id'+ str(y)
    y=y+1
    
    training_not_spam[id_count]= tokenized_email
     
#(c.1) opening test datasets
w=1
for filename in glob.glob(os.path.join(file_path_test, '*.txt')):

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
                
                tokenized_email.append(word)
                
        #print( tokenized_email)
    #Here we update the  ids (to use it in a dictionary)
    id_count= 'id'+ str(w)
    w=w+1
    
    test[id_count] = tokenized_email
    

'Now we do calculations'

for words_test in test:
    
    '(1) We calculate the number of test terms occurs in spam email (test term occurances)'
    
    #for spam emails
    term_occurances_dic_spam= wordTest_in_wordTrain(training_spam, test[words_test])
    sum_term_occurances_spam={}
    
    for term in term_occurances_dic_spam:
        sum_term_occurances_spam[term]=sum(term_occurances_dic_spam[term])
        
    #for non spam emails
    term_occurances_dic_not_spam= wordTest_in_wordTrain(training_not_spam, test[words_test])
    sum_term_occurances_not_spam={}
    
    for term in term_occurances_dic_not_spam:
        sum_term_occurances_not_spam[term]= sum(term_occurances_dic_not_spam[term])
        
    '(2)Total words in spam emails'
    
    sum_total_words_spam= sum(total_trainWords(training_spam))
    
    #Total words in non_spam emails
    sum_total_words_not_spam= sum(total_trainWords(training_not_spam))
    
    '(3) Total number of unique words in both spam and non spam emails'
    
    #for spam emails
    unique_words_spam= unique_words(training_spam)
    unique_words_number_spam= len(unique_words_spam)
    
    #form non spam emails
    unique_words_not_spam= []
    
    for word in unique_words(training_not_spam):
        if word not in unique_words_spam:
            unique_words_not_spam.append(word)
            
    unique_words_number_not_spam= len(unique_words_not_spam)
    
    total_unique_words = unique_words_number_spam + unique_words_number_not_spam
    
    '(4) Using Laplace smoothing to calculate terms likelihoods'
    
    #laplace smoothing for spam emails
    spam_laplace= laplace_smoothing_propabilities(sum_term_occurances_spam, sum_total_words_spam,total_unique_words)
    
    #laplace smoothing for non_spam emails
    not_spam_laplace= laplace_smoothing_propabilities(sum_term_occurances_not_spam, sum_total_words_not_spam,total_unique_words)
    
    
    '(5) Calculating likelihoods for spam and non spam emails'
    
    #for spam emails
    likelihood_spam= likelihood(spam_laplace, test[words_test])
    
    #for non_spam emails
    likelihood_not_spam= likelihood(not_spam_laplace, test[words_test])
    
    '(6) Calculating priors'
    prior_spam=len(training_spam)/(len(training_spam)+len(training_not_spam))
    prior_not_spam=len(training_not_spam)/(len(training_spam)+len(training_not_spam))
    
    '(7) Evidences for both spam and non spam emails'
    #set evedance=1 for both spam and non spam emails since they cancel out under posterirs division
    evidence_spam=1
    evidence_not_spam=1
    
    '(8) Naive Bayes equation to find posteriors for spam and non_spam emails'
    #posterior for spam emails
    posterior_spam= Naive_Bayes_eq(likelihood_spam, prior_spam,evidence_spam)
    

    #posterior for non_spam emails
    posterior_not_spam= Naive_Bayes_eq(likelihood_not_spam, prior_not_spam,evidence_not_spam)
    
    
    '(9) calculating probabilities for each class (spam or non spam)'
    ratio= posterior_spam/posterior_not_spam
    prob_spam= ratio/(1+ratio)
    prob_not_spam= 1-prob_spam
    print('\n probability that is a spam: ',prob_spam*100,'%', ' and probability that is not a spam: ',prob_not_spam*100,'%')