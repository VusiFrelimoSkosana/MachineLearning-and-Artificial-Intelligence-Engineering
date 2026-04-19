# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:23:03 2022
@author: Vusi Skosana
"""

# -*- coding: utf-8 -*-

"""
Created on Fri Sep  9 20:20:45 2022
@author: Vusi Skosana
"""

def Naive_Bayes_Eq(likelihood_S, prior_S, likelihood_NS, prior_NS):
    PS= likelihood_S * prior_S
    PNS= likelihood_NS * prior_NS
    ratio= PS/PNS
    prob_spam=ratio/(1+ratio)
    prob_not_spam=1-prob_spam
    return print('\n probability that is a spam: ',prob_spam*100,'%', ' and probability that is not a spam: ',prob_not_spam*100,'%')


#Below are training and test datasets
spam={'id1':['click','win','prize'], 'id2':['prize', 'free','prize'], 'id3':['click','prize','free']}
not_spam={'id1':['click','meeting','setup','meeting']}

words_test=['free','setup','meeting','free']

#below are parameters required to calculate probabilities of words
word_count_spam={k:[] for k in words_test}
word_count_not_spam={n:[] for n in words_test}

total_words_spam=[]
total_words_not_spam=[]

unique_words=[] #unique words in both spam and non spam emails


# (1) for SPAM emails
print('\n for spam emails')
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
    print(occurances_spam)
    
    #loop for repetitive of each word that occurs in all spam emails
    for word in occurances_spam:
        word_count_spam[word].append(occurances_spam[word])
        
    #loop for unique words in spam emails
    for unique in spam[id_number]:
        if unique not in unique_words:
            unique_words.append(unique)
        
print(word_count_spam)

print('total words per email: ', total_words_spam) 



#(2)for NON_SPAM emails
print('\n for non spam emails')

for id_number in not_spam: #loop that iterates over each NON_SPAM email

    #First we count total number of words in non_spam emails and sum them up
    total_words_not_spam.append(len(not_spam[id_number]))
    
    
    #Now we compute frequency of words in non_spam emails
    word_value_not_spam={}
    existing= not_spam[id_number]
    for term in existing: 
        if term not in word_value_spam:
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
           
    print(occurances_not_spam)
    
    #loop below for repetitive of each word that occurs in all spam emails
    for word in occurances_not_spam:
        word_count_not_spam[word].append(occurances_not_spam[word])
        
    #loop for unique words in non spam emails
    for unique in not_spam[id_number]:
        if unique not in unique_words:
            unique_words.append(unique)

print(word_count_not_spam)
print('total words in non spam email: ',total_words_not_spam)

print('\n for spam and non spam emails')
print('unique words in spam and non spam emails: ',unique_words)

#(3)Now we sum parameters for spam emails (into single value)
print('\n Now we sum parameters for spam emails (into single value)')

test_term_occurances_spam={}
total_term_frequency_spam= sum(total_words_spam)

total_unique_words_spam=len(unique_words) #this value is unique for both spam and non spam

for word in word_count_spam:
    
    test_term_occurances_spam[word]= sum(word_count_spam[word])

print('Test term occurances: ', test_term_occurances_spam)
print('Total term frequency: ',total_term_frequency_spam)
print('total unique words: ',total_unique_words_spam)

#(4)Now we sum parameters for non spam emails (into single value)
print('\n Now we sum parameters for non spam emails (into single value)')

test_term_occurances_not_spam={}
total_term_frequency_not_spam= sum(total_words_not_spam)


for word in word_count_not_spam :
    
    test_term_occurances_not_spam[word]= sum(word_count_not_spam[word])
    
print('Test term occurances: ', test_term_occurances_not_spam)
print('Total term frequency: ', total_term_frequency_not_spam)

#(5) Now we calculate probabilities (using laplace smoothing) for spam emails
print('\n probabilities (using laplace smoothing) for spam emails')
term_probabilities_spam={}

for word_occurances in test_term_occurances_spam:
    
    prob=(test_term_occurances_spam[word_occurances]+1)/(total_term_frequency_spam + total_unique_words_spam)
    term_probabilities_spam[word_occurances]=prob
print('Probabilities of words in spam emails(class): ',term_probabilities_spam)


#(6) Now we calculate probabilities (using laplace smoothing) for non spam emails
print('\n probabilities (using laplace smoothing) for non spam emails')
term_probabilities_not_spam={}

for word_occurances in test_term_occurances_not_spam:
    
    prob=(test_term_occurances_not_spam[word_occurances]+1)/(total_term_frequency_not_spam + total_unique_words_spam)
    term_probabilities_not_spam[word_occurances]=prob
print('Probabilities of words in non spam emails(class): ',term_probabilities_not_spam)


#(7) computing the priors
print('\n Computing Priors for spam and non spam emails(classes) ')

prior_S=len(spam)/(len(spam)+len(not_spam))
prior_NS=len(not_spam)/(len(spam)+len(not_spam))

print('Prior for spam emails: ', prior_S)
print('Prior for non spam emails: ', prior_NS)

#(8)computing the likelihoods
print('\n computing the likelihoods')

#likelihoods parameters from spam and non spam emails(classes)
likelihood_S={}
likelihood_NS={}   #last term in a dictionary gets overidden if is the same

#loop for spam likelihood
prob_product_spam=1
for word in words_test:
    prob_product_spam= prob_product_spam * term_probabilities_spam[word]
    likelihood_S[word]=prob_product_spam
    
print('spam likelihood: ', likelihood_S[words_test[-1]])
#print(likelihood_S)

#loop for spam likelihood
prob_product_not_spam=1
for word in words_test:
    prob_product_not_spam= prob_product_not_spam* term_probabilities_not_spam[word]
    likelihood_NS[word]=prob_product_not_spam
    
print('non spam likelihood: ', likelihood_NS[words_test[-1]])

Naive_Bayes_Eq(likelihood_S[words_test[-1]], prior_S, likelihood_NS[words_test[-1]], prior_NS)
