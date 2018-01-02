#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt


num_friends = [1, 2, 3, 4, 5, 6]
# ……等等许多
friend_counts = Counter(num_friends)
xs = range(6)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("Number of Friends")
plt.ylabel("Number of People")
plt.show()

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0] # 1
second_smallest_value = sorted_values[1] # 1
second_largest_value = sorted_values[-2] # 49



#均值
def mean(x):
    return sum(x) / len(x)

#中位数
def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # 如果是奇数， 返回中间值
        return sorted_v[midpoint]
    else:
        # 如果是偶数， 返回中间两个值的均值
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

#分位数：少于数据中特定百分比的一个值
def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

#众数
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]


# 极差， "range" 在Python中已经有特定的含义， 所以我们换一个不同的名字
def data_range(x):
    return max(x) - min(x)


# 方差
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squares(x):
    return sum([i ** 2 for i in x])

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))


#一种更加稳健的方案是计算 75% 的分位数和 25% 的分位数之差：
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

# 方差衡量了单个变量对均值的偏离程度，而协方差衡量了两个变量对均值的串联偏离程度
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
    for v_i, w_i in zip(v, w))

# 如果向量 x 和向量 y
# 的对应元素同时大于它们自身序列的均值，或者同时小于它们自身序列的均值，那将为求
# 和贡献一个正值。如果其中一个元素大于自身的均值，而另一个小于自身的均值，那将为
# 求和贡献一个负值。因此，如果协方差是一个大的正数，就意味着如果 y 很大，那么 x 也
# 很大，或者如果 y 很小，那么 x 也很小。如果协方差为负而且绝对值很大，就意味着 x 和
# y 一个很大，而另一个很小。接近零的协方差意味着以上关系都不存在。
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

# 相关是更常受到重视的概念，它是由协方差除以两个变量的标准差
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0