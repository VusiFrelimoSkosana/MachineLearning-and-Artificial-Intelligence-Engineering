# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:49:51 2022

@author: Professor
"""
#import django
#print(django.get_version())
#import speech_recognition
import pyttsx3
import nltk
from nltk.corpus import state_union

import spacy

print(spacy.__file__)

engine =pyttsx3.init()


#text= state_union.raw("2005-GWBush.txt")
#print(text)
  

"""RATE"""

rate =engine.getProperty('rate')
print(rate)
engine.setProperty('rate',145)

"""VOLUME"""

volume =engine.getProperty('volume') #case sensitive
print(volume)
engine.setProperty('Volume',1.0)


"""VOICE"""

voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #male  voice
#engine.setProperty('voice', voices[1].id)  #female voice

while True:
    inp = input("What do you want to say? say it! ")
    
    if inp=="done":
        engine.say(f"You have just said {inp}, goodbye")
        engine.runAndWait()
        break
    else:
        engine.say(f"you have just said {inp}")
        engine.runAndWait()
        continue



#engine.save_to_file('Hello world', 'test.mp3')