import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

question= "how are you, I would like to be part of this generation"

tokenized_word= word_tokenize(question)

four_words=[]
three_words=[]

for word in tokenized_word:
    
    if len(word)==4:
        four_words.append(word)
        
    elif len(word)==3:
        three_words.append(word)

print(four_words)
print(three_words)