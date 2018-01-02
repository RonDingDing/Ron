#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
import matplotlib.pyplot as plt

z = np.sqrt(xs ** 2 + ys ** 2)
# >>> z
# array([[ 7.07106781,  7.06400028,  7.05693985, ...,  7.04988652,
#          7.05693985,  7.06400028],
#        [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
#          7.04985815,  7.05692568],
#        [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
#          7.04278354,  7.04985815],
#        ...,
#        [ 7.04988652,  7.04279774,  7.03571603, ...,  7.0286414 ,
#          7.03571603,  7.04279774],
#        [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
#          7.04278354,  7.04985815],
#        [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
#          7.04985815,  7.05692568]])
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
plt.show()

############################################
# where: 若相应的cond为True，则该值为xarr相应值，反之则为yarr的相应值
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr)
# >>> result
# array([ 1.1,  2.2,  1.3,  1.4,  2.5])


arr = np.random.randn(4, 4)
# >>> arr
# array([[-0.50363384,  0.72567185,  1.53593853,  0.03115105],
#        [-2.52563316,  1.42037227,  0.44436279, -1.13713624],
#        [-0.47159406,  0.0775334 ,  0.16221634,  0.19668178],
#        [-0.1194568 , -1.24649166, -0.37561908,  1.15864719]])
a = np.where(arr > 0, 2, -2)
# # >>> a
# array([[-2,  2,  2,  2],
#        [-2,  2,  2, -2],
#        [-2,  2,  2,  2],
#        [-2, -2, -2,  2]])

arr = np.arange(20).reshape(5, 4)
# >>> arr
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15],
#        [16, 17, 18, 19]])
# >>> arr.mean()
# 9.5
# >>> np.mean(arr)
# 9.5
# >>> arr.sum()
# 190
# >>> arr.mean(axis=1)
# array([1.5, 5.5, 9.5, 13.5, 17.5])

# >>> from __future__ import division
# >>> np.array(
#     [(0 + 1 + 2 + 3) / 4, (4 + 5 + 6 + 7) / 4, (8 + 9 + 10 + 11) / 4, (12 + 13 + 14 + 15) / 4, (16 + 17 + 18 + 19) / 4])
# array([1.5, 5.5, 9.5, 13.5, 17.5])

# >>> arr.sum(0) #一列
# array([40, 45, 50, 55])
#
# >>> arr.sum(1) #一行
# array([ 6, 22, 38, 54, 70])


arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# >>> arr.cumsum()
# array([ 0,  1,  3,  6, 10, 15, 21, 28, 36])
# >>> arr.cumsum(0)
# array([[ 0,  1,  2],
#        [ 3,  5,  7],
#        [ 9, 12, 15]])
# >>> arr.cumsum(1)
# array([[ 0,  1,  3],
#        [ 3,  7, 12],
#        [ 6, 13, 21]])

# >>> arr.cumprod()
# array([0, 0, 0, 0, 0, 0, 0, 0, 0])
# >>> arr.cumprod(0)
# array([[ 0,  1,  2],
#        [ 0,  4, 10],
#        [ 0, 28, 80]])
# >>> arr.cumprod(1)
# array([[  0,   0,   0],
#        [  3,  12,  60],
#        [  6,  42, 336]])


# sum            对数组中全部或某轴向的元素求和。零长度的数组和为0
# mean           算术平均数，0长度的数组mean为NaN
# std var        标准差和方差，自由度可调（n）
# min, max       最大最小值
# argmin, argmax 最大和最小元素的索引
# cumsum         所有元素的累计和
# cumprod        所有元素的累计积


apple = np.random.randn(100)
# >>> (apple > 0)
# array([ True,  True,  True,  True, False,  True,  True, False, False,
#        False, False, False,  True,  True, False, False,  True, False,
#         True, False, False, False, False, False, False,  True,  True,
#         True, False, False, False, False,  True,  True,  True,  True,
#        False, False,  True, False, False, False, False,  True, False,
#        False,  True, False,  True,  True, False, False, False, False,
#         True, False,  True,  True,  True,  True, False,  True, False,
#         True, False,  True, False, False,  True,  True,  True,  True,
#        False,  True,  True, False, False, False, False,  True,  True,
#        False, False,  True, False,  True, False, False, False, False,
#        False, False, False, False, False, False, False,  True, False,  True], dtype=bool)
# >>> (apple > 0).sum()
# 42

# any: 类似any
# >>> bools = np.array([False, False, True, False])
# >>> bools.any()
# True
# >>>

# all: 类似all
# >>> bools.all()
# False

# >>> abb = np.random.randn(8)
# >>> abb
# array([-0.11755719, -1.14790394, -0.10110501, -0.2622101 , -1.14560842,
#        -0.09275236,  2.20007835, -1.07889309])
# >>> abb.sort()
# >>> abb
# array([-1.14790394, -1.14560842, -1.07889309, -0.2622101 , -0.11755719,
#        -0.10110501, -0.09275236,  2.20007835])
#
#
# >>> acc = np.random.randn(5,3)
# >>> acc
# array([[-0.85028678,  0.06151437,  1.02230907],
#        [ 0.16404089, -0.49186805, -2.19155645],
#        [-1.32034305,  1.93514681, -0.83476469],
#        [ 0.30879393,  2.12409155, -0.52242818],
#        [ 0.9568944 ,  0.13277934, -1.07822772]])
# >>> acc.sort(1)
# >>> acc
# array([[-0.85028678,  0.06151437,  1.02230907],
#        [-2.19155645, -0.49186805,  0.16404089],
#        [-1.32034305, -0.83476469,  1.93514681],
#        [-0.52242818,  0.30879393,  2.12409155],
#        [-1.07822772,  0.13277934,  0.9568944 ]])
# >>> acc.sort(0)
# >>> acc
# array([[-2.19155645, -0.83476469,  0.16404089],
#        [-1.32034305, -0.49186805,  0.9568944 ],
#        [-1.07822772,  0.06151437,  1.02230907],
#        [-0.85028678,  0.13277934,  1.93514681],
#        [-0.52242818,  0.30879393,  2.12409155]])

large_arr = np.random.randn(1000)
# >>> large_arr.sort()
# >>> large_arr[int(0.05 * len(large_arr))]
# -1.6527589251595762


# unique: 过滤重复元素
name = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# >>> np.unique(name)
# array(['Bob', 'Joe', 'Will'],
#       dtype='|S4')

# in1d:每个数字是否存在在第二个输入的参数中
values = np.array([6, 0, 0, 3, 2, 5, 6])
# >>> np.in1d(values, [2,3,6])
# array([ True, False, False,  True,  True, False,  True], dtype=bool)


# unique(x)         计算x中的唯一元素并返回有序结果
# intersect1d(x, y) 计算x和y中的公共元素，并返回有序结果
# union1d(x, y)     计算x和y的并集，并返回有序结果
# in1d(x, y)        得到一个表示“x的元素是否包含于y”的布尔型数组
# setdiff1d(x, y)   集合的差，即元素在x中且不在y中
# setxor1d(x, y)    集合的对称差，即存在于一个数组中，但不同时存在于两个数组中的元素
