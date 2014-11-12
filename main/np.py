#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np

ITEM_MAX_NUM = 8170 
USER_MAX_NUM = 7255 

tsv = csv.reader(file(r"../DBbook/DBbook_train_ratings/DBbook_train_ratings_no_col.tsv"), delimiter = '\t')

mat = np.zeros((ITEM_MAX_NUM, USER_MAX_NUM))
for row in tsv:
    user_id = int(row[0])-1
    item_id = int(row[1])-1
    val = int(row[2])
    mat[item_id][user_id] = val

print mat

np.savetxt("mat.csv", mat, delimiter=",")
    


