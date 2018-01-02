#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle

f= open("pickle_test.pkl",'rb')

a=pickle.load(f)
print(a)

b=pickle.load(f)
print(b.n)