#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
class Test(object):
    def __init__(self,n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["alex","rain","test"]

f= open("pickle_test.pkl",'wb')
pickle.dump(name,f)
pickle.dump(t2,f)
pickle.dump(t,f)
f.close()