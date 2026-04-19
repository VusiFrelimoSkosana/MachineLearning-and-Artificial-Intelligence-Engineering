# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 06:43:29 2022

@author: Professor
"""

from easyAI.vectorize import wordTest_in_wordTrain
from easyAI.vectorize import total_trainWords
from easyAI.vectorize import unique_words
from easyAI.probabilities import laplace_smoothing_propabilities
from easyAI.probabilities import likelihood
from easyAI.probabilities import Naive_Bayes_eq


#Below are training and test datasets
training_spam={'id1':['click','win','prize'], 'id2':['prize', 'free','prize'], 'id3':['click','prize','free']}
training_not_spam={'id1':['click','meeting','setup','meeting']}

words_test=['free','setup','meeting','free']
    

'(1) We calculate the number of test terms occurs in spam email (test term occurances)'

#for spam emails
term_occurances_dic_spam= wordTest_in_wordTrain(training_spam, words_test)
sum_term_occurances_spam={}

for term in term_occurances_dic_spam:
    summing=sum_term_occurances_spam[term]=sum(term_occurances_dic_spam[term])
    
    
#for non spam emails
term_occurances_dic_not_spam= wordTest_in_wordTrain(training_not_spam, words_test)
sum_term_occurances_not_spam={}

for term in term_occurances_dic_not_spam:
    summing=sum_term_occurances_not_spam[term]=sum(term_occurances_dic_not_spam[term])
    
print(sum_term_occurances_not_spam)
print(sum_term_occurances_spam)


'(2)Total words in spam emails'

sum_total_words_spam= sum(total_trainWords(training_spam))
print(sum_total_words_spam)

#Total words in non_spam emails
sum_total_words_not_spam= sum(total_trainWords(training_not_spam))
print(sum_total_words_not_spam)

'(3) Total number of unique words in both spam and non spam emails'

#for spam emails
unique_words_spam= unique_words(training_spam)
unique_words_number_spam=len(unique_words_spam)
print(unique_words_spam,unique_words_number_spam)

#form non spam emails
unique_words_not_spam= []

for word in unique_words(training_not_spam):
    if word not in unique_words_spam:
        unique_words_not_spam.append(word)
        
unique_words_number_not_spam=len(unique_words_not_spam)
print(unique_words_not_spam,unique_words_number_not_spam)

total_unique_words= unique_words_number_spam + unique_words_number_not_spam

print(total_unique_words)

'(4) Using Laplace smoothing to calculate terms likelihoods'

#laplace smoothing for spam emails
spam_laplace= laplace_smoothing_propabilities(sum_term_occurances_spam, sum_total_words_spam,total_unique_words)
print(spam_laplace)

#laplace smoothing for non_spam emails
not_spam_laplace= laplace_smoothing_propabilities(sum_term_occurances_not_spam, sum_total_words_not_spam,total_unique_words)
print(not_spam_laplace)

'(5) Calculating likelihoods for spam and non spam emails'

#for spam emails
likelihood_spam= likelihood(spam_laplace, words_test)
print(likelihood_spam)

#for non_spam emails
likelihood_not_spam= likelihood(not_spam_laplace, words_test)
print(likelihood_not_spam)

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
print(posterior_spam)

#posterior for non_spam emails
posterior_not_spam= Naive_Bayes_eq(likelihood_not_spam, prior_not_spam,evidence_not_spam)
print(posterior_not_spam)

'(9) calculating probabilities for each class (spam or non spam)'
ratio= posterior_spam/posterior_not_spam
prob_spam=ratio/(1+ratio)
prob_not_spam=1-prob_spam
print('\n probability that is a spam: ',prob_spam*100,'%', ' and probability that is not a spam: ',prob_not_spam*100,'%')