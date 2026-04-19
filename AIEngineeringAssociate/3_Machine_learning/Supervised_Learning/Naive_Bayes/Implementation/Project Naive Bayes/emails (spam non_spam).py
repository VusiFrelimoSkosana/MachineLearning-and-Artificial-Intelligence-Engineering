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
'''
spam={'id1':['click','win','prize'], 'id2':['prize', 'free','prize'], 'id3':['click','prize','free']}
not_spam={'id1':['click','meeting','setup','meeting'],'id2':['move','cool','meeting'],'id3':['click','win','prize'],'id4':['free','setup','meeting','free']}
test={'id1':['free','setup','meeting','free'],'id2':['see', 'prize','look'],'id3':['move','cool','meeting']}

'''
file_path_spam = 'spam'
file_path_not_spam = 'ham'
file_path_test='test'

stop_words=set(stopwords.words('english'))  #unuseful words like, the, is in etc

english_words= set(nltk.corpus.words.words())  #English words

#Below are data structures containing training and test data set
spam={}
not_spam={}

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
    
    spam[id_count]= tokenized_email

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
    
    not_spam[id_count]= tokenized_email
     
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

#NOW WE DO LANGUAGE PROCESSING AND COMPUTATION

#N.B in this case we will test multiple emails (accessing multiple files)
count_test=1
for words in test:
    print('email_'+str(count_test)+":")
    count_test=count_test+1
    
    words_test=test[words] #This is a test data structure (list)
    
    def Naive_Bayes_Eq(likelihood_S, prior_S, likelihood_NS, prior_NS):
        PS= likelihood_S * prior_S
        PNS= likelihood_NS * prior_NS
        ratio= PS/PNS
        prob_spam=ratio/(1+ratio)
        prob_not_spam=1-prob_spam
        return print('probability that is a spam: ',prob_spam*100,'%', ' and probability that is not a spam: ',prob_not_spam*100,'%'+'\n')

    #Below are training and test datasets
    
    #below are parameters required to calculate probabilities of words
    word_count_spam={k:[] for k in words_test}
    word_count_not_spam={n:[] for n in words_test}
    
    total_words_spam=[]
    total_words_not_spam=[]
    
    unique_words=[] #unique words in both spam and non spam emails
    
    # (1) for SPAM emails
    
    for id_number in spam: #loop that iterates over each SPAM email
       
        #First we count total number of words in spam emails and sum them up
        total_words_spam.append(len(spam[id_number]))
        
        #Now we compute frequency of words in spam emails
        word_value_spam={}
        existing= spam[id_number]
        for term in existing: 
            if term not in word_value_spam:
                word_value_spam[term]= existing.count(term)
           
        words=[]
        for element in word_value_spam:
            
            words.append(element)
        
        #loop for repetitive of each word that occurs in individual spam email
        occurances_spam={}
        
        for word_test in words_test: #N.B be mindful of 's' words and word test
            for word_spam in words:
                if word_test == word_spam:
                    occurances_spam[word_test]= word_value_spam[word_test]
    
                elif word_test not in words :
                    occurances_spam[word_test]= 0
        
        #loop for repetitive of each word that occurs in all spam emails
        for word in occurances_spam:
            word_count_spam[word].append(occurances_spam[word])
            
        #loop for unique words in spam emails
        for unique in spam[id_number]:
            if unique not in unique_words:
                unique_words.append(unique)
    
    #(2)for NON_SPAM emails
    
    for id_number in not_spam: #loop that iterates over each NON_SPAM email
    
        #First we count total number of words in non_spam emails and sum them up
        
        total_words_not_spam.append(len(not_spam[id_number]))
        
        
        #Now we compute frequency of words in non_spam emails
        word_value_not_spam={}
        existing= not_spam[id_number]
        for term in existing:
            if term not in word_value_not_spam:
                word_value_not_spam[term]= existing.count(term)
                
        

        words=[]
        for element in word_value_not_spam:
            words.append(element)
       
        #below we are trying to find repetitive words of test data to training not_spam data set
        occurances_not_spam={}
        
        for word_test in words_test:
            for word_not_spam in words:
                if word_test == word_not_spam:
                    occurances_not_spam[word_test]= word_value_not_spam[word_test]
                    
                elif word_test not in words :
                    occurances_not_spam[word_test]= 0
               
        #loop below for repetitive of each word that occurs in all spam emails
        for word in occurances_not_spam:
            word_count_not_spam[word].append(occurances_not_spam[word])
            
        #loop for unique words in non spam emails
        for unique in not_spam[id_number]:
            if unique not in unique_words:
                unique_words.append(unique)
                
    
    
    #(3)Now we sum parameters for spam emails (into single value)
    
    test_term_occurances_spam={}
    total_term_frequency_spam= sum(total_words_spam)
    
    total_unique_words_spam=len(unique_words) #this value is unique for both spam and non spam
    
   
    for word in word_count_spam:
        
        test_term_occurances_spam[word]= sum(word_count_spam[word])
    
    #(4)Now we sum parameters for non spam emails (into single value)
    
    test_term_occurances_not_spam={}
    total_term_frequency_not_spam= sum(total_words_not_spam)
    
   
    for word in word_count_not_spam :
        
        test_term_occurances_not_spam[word]= sum(word_count_not_spam[word])
      
    
    
    #(5) Now we calculate probabilities (using laplace smoothing) for spam emails
   
    term_probabilities_spam={}
    
    for word_occurances in test_term_occurances_spam:
        
        prob=(test_term_occurances_spam[word_occurances]+1)/(total_term_frequency_spam + total_unique_words_spam)
        term_probabilities_spam[word_occurances]=prob
    
     
    #(6) Now we calculate probabilities (using laplace smoothing) for non spam emails
    
    term_probabilities_not_spam={}
    
    for word_occurances in test_term_occurances_not_spam:
        
        prob=(test_term_occurances_not_spam[word_occurances]+1)/(total_term_frequency_not_spam + total_unique_words_spam)
        term_probabilities_not_spam[word_occurances]=prob
        
    
    #(7) computing the priors
    
    prior_S=len(spam)/(len(spam)+len(not_spam))
    prior_NS=len(not_spam)/(len(spam)+len(not_spam))
    
    #(8)computing the likelihoods
    
    #likelihoods parameters from spam and non spam emails(classes)
    likelihood_S={}
    likelihood_NS={}   #last term in a dictionary gets overwritten if is the same
    
    #loop for spam likelihood
    prob_product_spam=1
    for word in words_test:
        prob_product_spam= prob_product_spam * term_probabilities_spam[word]
        likelihood_S[word]=prob_product_spam
    
    #loop for spam likelihood
    prob_product_not_spam=1
    for word in words_test:
        prob_product_not_spam= prob_product_not_spam* term_probabilities_not_spam[word]
        likelihood_NS[word]=prob_product_not_spam
        
   
   
    Naive_Bayes_Eq(likelihood_S[words_test[-1]], prior_S, likelihood_NS[words_test[-1]], prior_NS)