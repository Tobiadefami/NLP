# Import Libraries

import spacy
nlp = spacy.load('en')
doc = nlp(u'I am flying to Frisco')
[w.text for w in doc]
