from operator import mul
from functools import partial
triple = partial(mul, 3)  
print(triple(7))  
#21
print(list(map(triple, range(1, 10))))
#[3, 6, 9, 12, 15, 18, 21, 24, 27]
