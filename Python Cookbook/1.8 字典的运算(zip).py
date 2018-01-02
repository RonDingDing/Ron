>>> prices = {"ACME": 45.23, "AAPL": 612.78,
              "IBM": 205.55, "HPQ":37.20, "FB":10.74}
>>> min_price = min(zip(prices.values(), prices.keys()))
>>> min_price
(10.74, 'FB')
>>> max_price = max(zip(prices.values(), prices.keys()))
>>> max_price
(612.78, 'AAPL')
>>> 
>>> prices_sorted = sorted(zip(prices.values(), prices.keys()))
>>> prices_sorted
[(10.74, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'),
 (205.55, 'IBM'), (612.78, 'AAPL')]
>>> 
>>> 
>>> prices_and_names = zip(prices.values(), prices.keys())
>>> print(min(prices_and_names))
(10.74, 'FB')
 
>>> 
>>> min(prices, key=lambda k: prices[k])
'FB'
>>> max(prices, key=lambda k: prices[k])
'AAPL'

################################################################################

>>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
>>> min(zip(prices.values(), prices.keys()))
(45.23, 'AAA')
>>> max(zip(prices.values(), prices.keys()))
(45.23, 'ZZZ')
>>> 
