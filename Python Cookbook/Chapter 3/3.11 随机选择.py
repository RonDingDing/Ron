import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
 

 
print(random.sample(values, 2))
 
 
random.shuffle(values)
print(values)
# [2, 4, 6, 5, 3, 1]
 

 

print(random.randint(0,10))
# 2
 

 

print(random.random())
# 0.9406677561675867
 

#如果要获取N位随机位(二进制)的整数，使用 random.getrandbits() ：

print(random.getrandbits(200))
# 335837000776573622800628485064121869519521710558559406913275
 
  
random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data

