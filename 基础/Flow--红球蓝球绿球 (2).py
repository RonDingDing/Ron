i = 100
while i <1000:
	a = list(str(i))[0]
	b = list(str(i))[1]
	c = list(str(i))[2]
	if i == (int(a) ** 3) + (int(b) ** 3) + (int(c) ** 3):
		print (i, end = " ")
	i = i + 1

input()
