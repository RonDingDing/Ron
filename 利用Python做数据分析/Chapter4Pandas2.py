

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year':[2000, 2001, 2002, 2001, 2002], 'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
# >>> DataFrame(data)
#    pop   state  year
# 0  1.5    Ohio  2000
# 1  1.7    Ohio  2001
# 2  3.6    Ohio  2002
# 3  2.4  Nevada  2001
# 4  2.9  Nevada  2002

DataFrame(data, columns=['year', 'state', 'pop'])
#    year   state  pop
# 0  2000    Ohio  1.5
# 1  2001    Ohio  1.7
# 2  2002    Ohio  3.6
# 3  2001  Nevada  2.4
# 4  2002  Nevada  2.9

DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
#        year   state  pop debt
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN


frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
# >>> frame2['year']
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64

# >>> frame2.year
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64

# >>> frame2.ix['three']
# year     2002
# state    Ohio
# pop       3.6
# debt      NaN
# Name: three, dtype: object

# >>> frame2
#        year   state  pop  debt
# one    2000    Ohio  1.5  16.5
# two    2001    Ohio  1.7  16.5
# three  2002    Ohio  3.6  16.5
# four   2001  Nevada  2.4  16.5
# five   2002  Nevada  2.9  16.5

frame2['debt'] = 16.5
# >>> frame2
#        year   state  pop  debt
# one    2000    Ohio  1.5  16.5
# two    2001    Ohio  1.7  16.5
# three  2002    Ohio  3.6  16.5
# four   2001  Nevada  2.4  16.5
# five   2002  Nevada  2.9  16.5

frame2['debt'] = np.arange(5.)
# >>> frame2
#        year   state  pop  debt
# one    2000    Ohio  1.5   0.0
# two    2001    Ohio  1.7   1.0
# three  2002    Ohio  3.6   2.0
# four   2001  Nevada  2.4   3.0
# five   2002  Nevada  2.9   4.0

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# >>> frame2['debt'] = val
# >>> frame2
#        year   state  pop  debt
# one    2000    Ohio  1.5   NaN
# two    2001    Ohio  1.7  -1.2
# three  2002    Ohio  3.6   NaN
# four   2001  Nevada  2.4  -1.5
# five   2002  Nevada  2.9  -1.7

frame2['eastern'] = frame2.state == 'Ohio'
# >>> frame2
#        year   state  pop  debt  eastern
# one    2000    Ohio  1.5   NaN     True
# two    2001    Ohio  1.7  -1.2     True
# three  2002    Ohio  3.6   NaN     True
# four   2001  Nevada  2.4  -1.5    False
# five   2002  Nevada  2.9  -1.7    False
# >>> del frame2['eastern']
# >>> frame2.columns
# Index([u'year', u'state', u'pop', u'debt'], dtype='object')