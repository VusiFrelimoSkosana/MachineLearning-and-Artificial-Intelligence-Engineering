#learnt from Sentdex channel on Youtube#

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example_sentence= "I would like to pyhon as I am pythoning before being pythoned by a pythoner first"

words= word_tokenize(example_sentence)

for w in words:
    print(PorterStemmer().stem(w))