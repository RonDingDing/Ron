data = [[col for col in range(4)]]

data = [[1, 3, 5, 7], [7, 5, 3, 1], [2, 4, 6, 8], [8, 6, 4, 2]]


for i in data:
    print(i)
print("\n\n")
"""
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
"""

for rIndex, row in enumerate(data):
    for cIndex in range(rIndex,len(row)):
       data[cIndex][rIndex], data[rIndex][cIndex] = data[rIndex][cIndex], data[cIndex][rIndex]
        
        

for i in data:
    print(i)

"""
[0, 0, 0, 0]
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]
"""
