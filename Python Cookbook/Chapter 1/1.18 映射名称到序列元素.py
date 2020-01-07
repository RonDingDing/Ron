from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)
# 'jonesy@example.com'
print(sub.joined)
# '2012-10-19'

print(len(sub))
# 2
addr, joined = sub
print(addr)
# 'jonesy@example.com'
print(joined)
# '2012-10-19'


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
Stock(name='ACME', shares=100, price=123.45)
# s.shares = 75
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

s = s._replace(shares=75)
print(s)



from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
