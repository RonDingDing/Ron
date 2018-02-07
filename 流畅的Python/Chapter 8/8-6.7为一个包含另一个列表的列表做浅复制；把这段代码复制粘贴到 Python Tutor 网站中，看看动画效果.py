l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) # ➊
l1.append(100) # ➋
l1[1].remove(55) # ➌
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] # ➍
l2[2] += (10, 11) # ➎
print('l1:', l1)
print('l2:', l2)