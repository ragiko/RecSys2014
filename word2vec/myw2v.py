#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import word2vec

data = word2vec.Text8Corpus('../mydata/corpus.txt')

model = word2vec.Word2Vec(data, size=200)

print sum(model['fiction'])

# out=model.most_similar(positive=[u'fiction'])
# for x in out:
#         print x[0].encode("utf-8"), x[1]
