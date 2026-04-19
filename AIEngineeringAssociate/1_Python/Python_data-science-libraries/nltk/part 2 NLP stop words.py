#learnt from Sentdex channel on Youtube#

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

example_sentence= "This is an example showing off stop word filtration"

stop_words= set(stopwords.words('english'))

unfiltration=[]
print("these are filtered words: ", stop_words, "\n")


for w in word_tokenize(example_sentence):
    if w not in stop_words:
        unfiltration.append(w)


print("these are unfiltered words: ", unfiltration)

sentence='this , put it! or just do it... is this now?'