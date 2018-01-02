class How():
	def __new__(self, *arg):
		able = tuple(arg)
		if len(able) == 0:
			return "并没有传入参数"
		else:
			print ("传入了%s个参数，分别是：" % len(able), end = " ")
			for each in able:
				print(each, end = " ")
