#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
import re

t = """I need to find the computer name of one PC connected in LAN (joined to domain).
I have the IP address of terminal. how i will find the computername?
kindly advice 
"""

# http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk
tokens = nltk.word_tokenize(t)

# delete symbol
stops = set(stopwords.words('english'))
tokens = [t for t in tokens if t.lower() not in stops]

# delete symbol
tokens = [t for t in tokens if not re.match("^\W+$", t)]

print tokens

## tokens = nltk.word_tokenize(t)
## text = nltk.Text(tokens)
## fdist = nltk.FreqDist(text)
## 
## print fdist
