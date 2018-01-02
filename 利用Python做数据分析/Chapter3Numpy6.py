#! /usr/bin/env python
# -*- coding: utf-8 -*-
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 5], [4, 3], [2, 1]])
# >>> x
# array([[1, 2, 3],
#        [4, 5, 6]])
# >>> y
# array([[6, 5],
#        [4, 3],
#        [2, 1]])

# >>> np.dot(x,y)
# array([[20, 14],
#        [56, 41]])
# >>> x.dot(y)
# array([[20, 14],
#        [56, 41]])


# >>> np.dot(x, np.ones(3))
# array([  6.,  15.])

#
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 对角线
# >>> np.diag(x)
# array([1, 5, 9])

# 对角线的和
# >>> np.trace(x)
# 15