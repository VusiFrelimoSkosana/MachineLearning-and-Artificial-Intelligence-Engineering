#learnt from Sentdex channel on Youtube#

import nltk
#nltk.download()


#nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing - word tokenizers... sentence tokenizers
#lexicon and corporas
#corparas- body of text. ex: medical journals, presidential speeches, English language
#lexicons - words and their means

#investor-speak... regular english speaker

#investor speak 'bull' = someone who is posotive about the market
#english speak ;bull' = scary animal you don't want running @ you

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinksh-blue"

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)