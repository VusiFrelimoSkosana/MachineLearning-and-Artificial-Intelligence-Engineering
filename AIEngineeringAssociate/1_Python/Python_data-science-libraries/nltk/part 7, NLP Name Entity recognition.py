# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 15:50:00 2022

@author: Professor
"""
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
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

text="I stay here in South Africa and later on I would like smoth to stay kick in the United States of America for temporarly. Well and accomplish all my goal and be happy with my life. This will definately happen"

word_tokens=  word_tokenize(text)
pos= pos_tag(word_tokens)

nameEnt = ne_chunk(pos)
nameEnt.draw()
