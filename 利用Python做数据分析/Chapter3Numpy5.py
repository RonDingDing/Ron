#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

arr = np.arange(10)

# save:保存至文件
# load:从文件中读取
np.save('some_array', arr)
# >>> np.load('some_array.npy')
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# savez:保存多个数列
np.savez('array_archive.npz', a=arr, b=arr)
# >>> arch = np.load('array_archive.npz')
# >>> arch['b']
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> arch['a']
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

with open('array_ex.txt', 'w')as f:
    f.writelines('1,2,3,4,5,6,7,8\n')
    f.writelines('8,7,6,5,4,3,2,1\n')

# loadtxt:从txt中获取数据
arr = np.loadtxt('array_ex.txt', delimiter=',')
# >>> arr
# array([[1., 2., 3., 4., 5., 6., 7., 8.],
#        [8., 7., 6., 5., 4., 3., 2., 1.]])
np.savetxt('array_ex.txt', arr)
# 'array_ex.txt'内容为
# 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00 5.000000000000000000e+00 6.000000000000000000e+00 7.000000000000000000e+00 8.000000000000000000e+00
# 8.000000000000000000e+00 7.000000000000000000e+00 6.000000000000000000e+00 5.000000000000000000e+00 4.000000000000000000e+00 3.000000000000000000e+00 2.000000000000000000e+00 1.000000000000000000e+00
