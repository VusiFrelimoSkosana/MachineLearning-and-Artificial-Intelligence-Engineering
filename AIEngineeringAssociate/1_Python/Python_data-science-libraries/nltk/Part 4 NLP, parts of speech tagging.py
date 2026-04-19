#learnt from Sentdex channel on Youtube#

import nltk
from nltk import pos_tag

"""
parts of speech tagging (pos tagging). the list is as follows:

NNP Proper noun, singular
NN Noun, singular  or mass
RB Adverb
VBD Verb, past tense
VBG Verb, gerund or present participle
JJ adjective
PRP Personal pronoun

"""

words=['fast',"good","car","move", "loved"]
print(pos_tag(words))












"""
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

train_text= state_union.raw("2005-GWBush.txt")
sample_text= state_union.raw("2006-GWBush.txt")

#print(sample_text)
#print(train_text)

custom_sent_tokenizer= PunktSentenceTokenizer(train_text)


tokenized= custom_sent_tokenizer.tokenize(sample_text)

#print(tokenized)

for sent in tokenized:
    words= nltk.word_tokenize(sent)  #list
    tagging= nltk.pos_tag(words)  #goes through a list and identify pos
    #print(tagging)


#mine=PunktSentenceTokenizer()

"""
    


