from pandas import Series
import pandas as pd

obj = Series([4, 7, -5, 3])
# >>> obj
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64

# obj.values
# >>> array([ 4,  7, -5,  3], dtype=int64)
# obj.index
# >>> RangeIndex(start=0, stop=4, step=1)


obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# >>> obj2
# d    4
# b    7
# a   -5
# c    3
# dtype: int64

# >>> obj2.index
# Index([u'd', u'b', u'a', u'c'], dtype='object')

# >>> obj2['a']
# -5
#
# >>> obj2['d']=6
# >>> obj
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64
# >>> obj2
# d    6
# b    7
# a   -5
# c    3
# dtype: int64
#
# >>> obj2[['c', 'a', 'd']]
# c    3
# a   -5
# d    6
# dtype: int64
# >>>
# >>>
# >>>
# >>>
# >>> obj2[obj2 > 0]
# d    6
# b    7
# c    3
# dtype: int64
# >>>
# >>> obj2 * 2
# d    12
# b    14
# a   -10
# c     6
# dtype: int64
# >>>
# >>> np.exp(obj2)
# d     403.428793
# b    1096.633158
# a       0.006738
# c      20.085537
# dtype: float64


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# >>> obj = Series(sdata)
# >>> obj3 = Series(sdata)
# >>> obj3
# Ohio      35000
# Oregon    16000
# Texas     71000
# Utah       5000
# dtype: int64

states = ['California', 'Ohio', 'Oregon', 'Texas']
# >>> obj4 = Series(sdata, index=states)
# >>> obj4
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# dtype: float64

# >>> pd.isnull(obj4)
# California     True
# Ohio          False
# Oregon        False
# Texas         False
# dtype: bool

# >>> pd.notnull(obj4)
# California    False
# Ohio           True
# Oregon         True
# Texas          True
# dtype: bool


# >>> obj3 + obj4
# California         NaN
# Ohio           70000.0
# Oregon         32000.0
# Texas         142000.0
# Utah               NaN
# dtype: float64


# >>> obj4
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# dtype: float64
# >>> obj4.name = 'population'

# >>> obj4.index.name = 'state'
# >>> obj4
# state
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# Name: population, dtype: float64