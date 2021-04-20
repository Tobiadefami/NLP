# Import Libraries
import spacy
from spacy.symbols import ORTH, LEMMA

# Create the nlp instance
nlp = spacy.load('en')

# tokenization
doc = nlp(u'I am flying to Frisco')
[w.text for w in doc]

# lemmatization
doc2 = nlp(u'this product integrates both libraries\
           for downloading and installing patches')
for token in doc2:
    print(token.text, token.lemma_)

# Applying lemmatization for meaning recognition
# add special case rules to an existing tokenizer
special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
[w.lemma_ for w in nlp(u'I am flying to Frisco')]

# Part of speech tagging
doc3 = nlp(u'I have flown to LA. Now I am flying to Frisco')
[w.text for w in doc3 if w.tag_ == "VBG" or w.tag_ == "VB"]
