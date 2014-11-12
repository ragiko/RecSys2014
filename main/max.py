#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
 

# maxを調べる

tsv = csv.reader(file(r"../DBbook/DBbook_train_ratings/DBbook_train_ratings.tsv"), delimiter = '\t')


a = []

for row in tsv:
    if (row[0] != "DBbook_userID"):
        a.append(int(row[0]))

tsv = csv.reader(file(r"../DBbook/task1_useritem_evaluation_data.tsv"), delimiter = '\t')

b = []

for row in tsv:
    if (row[0] != "DBbook_userID"):
        b.append(int(row[0]))

c = a + b
        

print max(c)

# return 7255
