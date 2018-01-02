#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import math


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors向量总和除以向量个数"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


# 点乘衡量了向量 v 在向量 w 方向延伸的程度。例如，如果 w = [1, 0] ，则 dot(v, w) 就是 v
# 的第一个元素。点乘的另一个解释是将 v 在 w 上投影所得到的向量的长度（如图 4-2） ：
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return magnitude(vector_subtract(v, w))


###################################################
# 矩阵
A = [[1, 2, 3],  # A有2行3列
     [4, 5, 6]]

B = [[1, 2],  # B有3行2列
     [3, 4],
     [5, 6]]


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # 第一行中元素的个数
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]  # 对每个A_i行获取第A_i行的第j个元素


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows * num_cols matrix
    whose(i, j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)             # 根据i创建一个列表
             for j in range(num_cols)]  # [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # 为每一个i创建一个列表

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

# [[1, 0, 0, 0, 0],
# [0, 1, 0, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1]]


