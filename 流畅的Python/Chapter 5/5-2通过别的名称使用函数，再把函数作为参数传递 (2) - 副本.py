def factorial(n): 
	'''returns n!'''
	return 1 if n < 2 else n * factorial(n-1)

fact = factorial 
print(fact)
#<function factorial at 0x...>
print(fact(5))
#120
print(map(factorial, range(11)))
#<map object at 0x...>
print(list(map(fact, range(11))))
#[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
