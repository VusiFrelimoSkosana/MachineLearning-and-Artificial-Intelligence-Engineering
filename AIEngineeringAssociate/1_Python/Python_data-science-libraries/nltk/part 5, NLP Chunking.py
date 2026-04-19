# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:01:16 2022

@author: Professor
"""

import nltk
#from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk import pos_tag


#text=state_union.raw('2006-GWBush.txt')

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
#print(pos)


chunkGram= "Chunk: {<RB.?>*<VBD.?>*<VB>+<NN>?}"


chunkParser = nltk.RegexpParser(chunkGram)
chunked=chunkParser.parse(pos)
chunked.draw()



#The entire code not yet working