#!/usr/bin/env python3

import sys
import spacy
import re
from spacy import displacy
from spacy.symbols import num

myfile = open(sys.argv[1]).read()

nlp = spacy.load('pt_core_news_sm')

myfile = re.sub(r"\n\s*\n", "===", myfile)

myfile = re.sub(r"\n", " ", myfile)

myfile = re.sub(r"===", "\n\n", myfile)

doc = nlp(myfile)

tokens = []

for token in doc.ents:  # NER
    print(token.text, token.start_char, token.end_char, token.label_)

for token in doc: # Tagger
    print(token.text, token.tag_)


