def factorial(n): 
	'''returns n!'''
	return 1 if n < 2 else n * factorial(n-1)
	
print(factorial(42))
#1405006117752879898543142606244511569936384000000000
print(factorial.__doc__)
#'returns n!'
print(type(factorial))
#<class 'function'>
