from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
# 2232 days, 11:02:10.846640

print(z)
# 2018-10-31 11:02:58.514532
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)
# Wednesday October 31, 2018


# 更快
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))