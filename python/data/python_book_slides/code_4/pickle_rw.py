
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open
import pickle

data = {'a': [1, 2, 3, 4],
       'John': 'abcdef',
       334455: 778899,
       'default': None}

with open('pickle_rw.bin', 'wb') as fout:
    pickle.dump(data, fout)

with open('pickle_rw.bin', 'rb') as fin:
    d = pickle.load(fin)
    print(d['John'])
    print(d[334455])
    

