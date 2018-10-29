
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


def avg(sequence):
    if isinstance(sequence, list) or isinstance(sequence, tuple) or isinstance(sequence, set):
        return sum(sequence)/len(sequence)


grades = 1, 2, 3, 5, 6
print(drop_first_last(grades))
# 3.3333333333333335
print((1+2+3+5+6)/5)
# 3.4
print((2+3+5)/3)
# 3.3333333333333335

#########################################################################

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
# 'Dave'
print(email)
# 'dave@example.com'
print(phone_numbers)
# ['773-555-1212', '847-555-1212']

#########################################################################

sales_record = [1, 32, 34, 45, 53]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)


def avg_comparison(trailing_avg, current_qtr):
    return True if trailing_avg > current_qtr else False


print(trailing_qtrs)
# [1, 32, 34, 45]
print(current_qtr)
# 53
print(avg_comparison(trailing_avg, current_qtr))
# False

#########################################################################

records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# foo 1 2
# bar hello
# foo 3 4

#########################################################################

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
# 'nobody'
print(homedir)
# '/var/empty'
print(sh)
# 'usr/bin/false'

#########################################################################

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
# 'ACME'
print(year)
# 2012

#########################################################################

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
# 1
print(tail)
# [10, 7, 4, 5, 9]

#########################################################################


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
# 36
