import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
# [2 4 6 8]
print(ax + 10)
# [11 12 13 14]
print(ax + ay)
# [ 6  8 10 12]
print(ax * ay)
# [ 5 12 21 32]

def f(x):
    return 3*x**2 - 2*x + 7
 
print(f(ax))
# [ 8 15 28 47]

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)

# [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  ...
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]]

grid += 10
print(grid)
# [[10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  ...
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]]

 

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Select row 1
print(a[1])
# [5 6 7 8]

# Select column 1
print( a[:,1])
# [ 2  6 10]

#  Select a subregion and change i
a[1:3, 1:3]
# [[ 6  7]
#  [10 11]]
a[1:3, 1:3] += 10
print(a)
# [[ 1  2  3  4]
#  [ 5 16 17  8]
#  [ 9 20 21 12]]

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
# [[101 103 105 107]
#  [105 117 119 111]
#  [109 121 123 115]]
print(a)
# [[ 1  2  3  4]
#  [ 5 16 17  8]
#  [ 9 20 21 12]]

#   Conditional assignment on an array
np.where(a < 10, a, 10)
# [[ 1  2  3  4]
#  [ 5 10 10  8]
#  [ 9 10 10 10]]
 