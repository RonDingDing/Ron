>>> from collections import deque
>>> 
>>> def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for li in lines:
		if pattern in li:
			yield li, previous_lines
		previous_lines.append(li)

>>> with open(r'somefile.txt') as f:
	for line, prevlines in search(f, 'python', 5):
		for pline in prevlines:
			print(pline)
		print(line)
		print("-" * 20)

		
line 1 python

--------------------
line 1 python

line 2 pythonic

--------------------
line 1 python

line 2 pythonic

line 3 pythoner

--------------------
line 1 python

line 2 pythonic

line 3 pythoner

line 4 pythoner

--------------------
line 1 python

line 2 pythonic

line 3 pythoner

line 4 pythoner

line 5 python

--------------------
line 1 python

line 2 pythonic

line 3 pythoner

line 4 pythoner

line 5 python

line 6 pythonic

--------------------
line 2 pythonic

line 3 pythoner

line 4 pythoner

line 5 python

line 6 pythonic

line 7 pythoner

--------------------
line 3 pythoner

line 4 pythoner

line 5 python

line 6 pythonic

line 7 pythoner

line 8 pythoner
--------------------

############################################################

>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
>>> q.append(5)
>>> q
deque([3, 4, 5], maxlen=3)

############################################################

>>> q = deque()
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3])
>>> q.appendleft(4)
>>> q
deque([4, 1, 2, 3])
>>> q.pop()
3
>>> q
deque([4, 1, 2])
>>> q.popleft()
4
>>> q
deque([1, 2])
>>> 
