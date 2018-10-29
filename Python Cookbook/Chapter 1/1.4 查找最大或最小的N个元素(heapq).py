
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
# [42, 37, 23]
print(heapq.nsmallest(3, nums))
# [-4, 1, 2]

############################################################
 
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
                 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                 {'name': 'FB', 'shares': 200, 'price': 21.09},
                 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                 {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
# [{'name': 'YAHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]

############################################################

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heapq.heapify(nums)
#把nums转化成heap堆数据结构
#堆数据结构最重要的特征是  heap[0] 永远是最小的元素。
#并且剩余的元素可以很容易的
#通过调用  heapq.heappop() 方法得到，
#该方法会先将第一个元素弹出来
nums
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8] 
print(heapq.heappop(nums))
# -4
print(heapq.heappop(nums))
# 1
print(heapq.heappop(nums))
# 2
 
