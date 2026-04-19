# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:14:26 2022

@author: Professor
"""

def laplace_smoothing_propabilities(test_term_occurances,total_term_frequency,total_unique_words):
    
    term_probabilities_likelihoods={}
    
    for word_occurances in test_term_occurances:
            
        prob=(test_term_occurances[word_occurances]+1)/(total_term_frequency + total_unique_words)
        term_probabilities_likelihoods[word_occurances]=prob
       
            
    return term_probabilities_likelihoods
    
def likelihood(term_probabilities_likelihoods, words_test):
    likelihood_dic={} #last term in a dictionary gets overidden if is the same
   
    #loop for likelihood
    prob_product=1
    for word in words_test:
        prob_product= prob_product * term_probabilities_likelihoods[word]
        likelihood_dic[word]= prob_product
        
    final_likelihood= likelihood_dic[words_test[len(words_test)-1]]
    
    return final_likelihood

def Naive_Bayes_eq(likelihood, prior, evidence):
    posterior= (likelihood * prior)/evidence
    return posterior
        

