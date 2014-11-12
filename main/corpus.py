#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
word2vec用のcorpas作成
"""

import nltk
from nltk.corpus import stopwords
import re
import csv

# 概要のインポート
tsv = csv.reader(file(r"../DBbook/DBbook_Items_DBpedia_mapping_abst.tsv"), delimiter = '\t')

docs = []

for row in tsv:
    docs.append(row[3].decode("utf-8"))

# ボキャブラリーのインポート
csv = csv.reader(file(r"../mydata/words.csv"), delimiter = ',')

for row in csv:
    vocab = row

result = []

for doc in docs:
    # http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk
    tokens = nltk.word_tokenize(doc)

    # ステミング
    # TODO: ここらへんの処理はオブジェクト化
    porter = nltk.PorterStemmer()
    tokens = [porter.stem(t) for t in tokens]

    doc_str = ' '.join([t.encode("utf-8") for t in tokens if t.encode("utf-8") in vocab])
    print doc_str
  
