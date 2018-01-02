
>>> import heapq
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> print(heapq.nlargest(3, nums))
[42, 37, 23]
>>> print(heapq.nsmallest(3, nums))
[-4, 1, 2]

################################################################################

 
>>> portfolio = [{'name': 'IBM' , 'shares': 100, 'price': 91.1},
                 {'name': 'AAPL', 'shares': 50,  'price': 543.22},
                 {'name': 'FB'  , 'shares': 200, 'price': 21.09},
                 {'name': 'HPQ ', 'shares': 35,  'price': 31.75},
                 {'name': 'YHOO', 'shares': 45,  'price': 16.35},
                 {'name': 'ACME', 'shares': 75,  'price': 115.65}]
>>> cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
>>> cheap
[{'name': 'YHOO', 'shares': 45,  'price': 16.35},
 {'name': 'FB',   'shares': 200, 'price': 21.09},
 {'name': 'HPQ',  'shares': 35,  'price': 31.75}]
>>> expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
>>> expensive
[{'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'ACME', 'shares': 75, 'price': 115.65},
 {'name': 'IBM',  'shares': 100,'price': 91.1}]

################################################################################

>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> import heapq
>>> heapq.heapify(nums)
>>> nums
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
>>> heapq.heapify(nums)
>>> heapq.heappop(nums)
-4
>>> heapq.heappop(nums)
1
>>> heapq.heappop(nums)
2

####删掉最小的三个数据
################################################################################

>>> import heapq
>>> 
>>> class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

		
>>> class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0
	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1
	def pop(self):
		return heapq.heappop(self._queue)[-1]

	
>>> class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

	
>>> q = PriorityQueue()
>>> q.push(Item('foo'), 1)
>>> q.push(Item('bar'), 5)
>>> q.push(Item('spam'), 4)
>>> q.push(Item('grok'), 1)
>>> q.pop()
Item('bar')
>>> q.pop()
Item('spam')
>>> q.pop()
Item('foo')
>>> q.pop()
Item('grok') 
"""
    在上面代码中，队列包含了一个  (-priority, index, item) 的元组。 优先级为负数的目的
是使得元素按照优先级从高到低排序。 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
    index 变量的作用是保证同等优先级元素的正确排序。 通过保存一个不断增加的  index
下标变量，可以确保元素安装它们插入的顺序排序。 而且，  index 变量也在相同优先级
元素比较的时候起到重要作用。
    为了阐明这些，先假定Item实例是不支持排序的：
>>> a = Item('foo')
>>> b = Item('bar')
>>> a < b
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unorderable types: Item() < Item()
>>>
    如果你使用元组  (priority, item) ，只要两个元素的优先级不同就能比较。 但是如果两
个元素优先级一样的话，那么比较操作就会跟之前一样出错：
>>> a = (1, Item('foo'))
>>> b = (5, Item('bar'))
>>> a < b
True
>>> c = (1, Item('grok'))
>>> a < c
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unorderable types: Item() < Item()
>>>
    通过引入另外的  index 变量组成三元组  (priority, index, item) ，就能很好的避免上面
的错误， 因为不可能有两个元素有相同的  index 值。Python在做元组比较时候，如果前
面的比较以及可以确定结果了， 后面的比较操作就不会发生了：
>>> a = (1, 0, Item('foo'))
>>> b = (5, 1, Item('bar'))
>>> c = (1, 2, Item('grok'))
>>> a < b
True
>>> a < c
True
>>>
    如果你想在多个线程中使用同一个队列，那么你需要增加适当的锁和信号量机制。 可以
查看12.3小节的例子演示是怎样做的。
""" 
