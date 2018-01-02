#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

memo = np.arange(10)
# sqrt: 给序列中的所有元素开方
# >>> np.sqrt(memo)
# array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
#         2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ])

# exp: 给序列中的所有元素做e的n次幂运算
# >>> np.exp(memo)
# array([  1.00000000e+00,   2.71828183e+00,   7.38905610e+00,
#          2.00855369e+01,   5.45981500e+01,   1.48413159e+02,
#          4.03428793e+02,   1.09663316e+03,   2.98095799e+03,
#          8.10308393e+03])



# >>> math.exp(2)
# 7.38905609893065
# >>> np.exp(2)
# 7.3890560989306504


x = np.arange(8)
y = np.array(sorted(range(8), reverse=True))

# maximum: 各取最大值放入array
# >>> np.maximum(x, y)
# array([7, 6, 5, 4, 4, 5, 6, 7])

# modf: 各取小数点后放入array, 各取小数点前放入array
# >>> np.modf(x)
# (array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]), array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.]))


# abs, fabs:         计算整数、浮点数或复数的绝对值，对于非复数值用fabs
# sqrt:              计算各元素的平方根，arr**0.5
# square:            计算各元素的平方，arr**2
# exp:               计算各元素的指数e**x
# log, log10,        自然对数（底数为e）、底数为10
# log2, log1p        底数为2，底数为2的（1+x
# sign               计算各元素的正负号：1为正数，0，-1为负数
# ceil               计算各元素的ceiling值，大于等于该值的最小整数
# floor              计算各元素的floor值，小于等于该值的最大整数
# rint               计算各元素的四舍五入，保留dtype
# modf               将数组的小数和整数部分以两个独立数组的形式返回
# isnan              返回一个表示哪些是“NaN”的布尔型数组
# isfinite           返回“那些元素是有穷的（非inf,非Nan）”的布尔型数组
# isinf              返回“那些元素是无穷的”的布尔型数组
# cos,cosh,
# sin,sinh
# tan,tanh           普通型和双曲型三角函数
# arccos, arccosh
# arcsin, arcsinh
# arctan, arctanh    反三角函数
# logical_not        计算各元素 not x的真值，-arr


# 二元函数
# add                将数组中的对应元素相加
# subtract           从第一个数组中减去第二个数组的元素
# multiply           数组元素相乘
# divide,floor_divide除法或地板除
# power              第一个数组元素的第二个数组元素次幂
# maximum, fmax      元素级的最大值计算，fmax忽略NaN
# minimum, fmin      元素级的最小值计算，fmin忽略NaN
# mod                元素级的求模元算
# copysign           将第二个数组中值的符号复制给第一个数组中的值
# greater            >
# greater_equal      >=
# less               <
# less_equal         <=
# equal              ==
# not_equal          !=
# logical_and        &
# logical_or         |
# logical_xor        ^异或运算
