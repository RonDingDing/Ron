from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
# 2
print(c.seconds)
# 37800
print(c.seconds / 3600)
# 10.5
print(c.total_seconds() / 3600)
# 58.5

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
# 2012-10-03 00:00:00
 
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
# 89
now = datetime.today()
print(now)
# 2018-10-31 10:53:00.133960
print(now + timedelta(minutes=10))
# 2018-10-31 11:03:00.133960


a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
# 2 days, 0:00:00
print((a - b).days)
# 2
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)
# 1

 