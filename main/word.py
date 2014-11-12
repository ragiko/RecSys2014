#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
V = 1500のwordを決定
"""

import nltk
from nltk.corpus import stopwords
import re
import csv

tsv = csv.reader(file(r"../DBbook/DBbook_Items_DBpedia_mapping_abst.tsv"), delimiter = '\t')

docs = []
for row in tsv:
    docs.append(row[3].decode("utf-8"))


words = []

for doc in docs:
    # http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk
    tokens = nltk.word_tokenize(doc)

    # nomalize lower words 
    tokens = [t.lower() for t in tokens]

    # delete priod 
    tokens = [t.encode("utf-8").translate(None, ".").decode("utf-8") for t in tokens]

    # ステミング
    porter = nltk.PorterStemmer()
    tokens = [porter.stem(t) for t in tokens]
    
    # delete stop
    stops = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stops]
    
    # delete symbol
    tokens = [t for t in tokens if not re.match("^\W+$", t)]

    # １文字削除
    tokens = [t for t in tokens if not re.match("^\w$", t)]

    # 空白を削除
    tokens = [t for t in tokens if not re.match("^$", t)]

    # delete number 
    tokens = [t for t in tokens if not re.match("^\d+$", t)]

    words += tokens

text = nltk.Text(words)
fdist = nltk.FreqDist(text)
result = [f.encode("utf-8") for f in fdist.keys()[:1500]]

writer = csv.writer(open('../mydata/words.csv', 'wb'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(result)

print fdist.keys()[:1500]
    
