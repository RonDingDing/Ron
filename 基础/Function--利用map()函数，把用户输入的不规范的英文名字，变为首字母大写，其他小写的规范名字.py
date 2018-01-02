def normalize(name):
    return list(map(lambda name: name.casefold().capitalize(), name))

#lambda函数把所有字符串变成小写，然后把第一个字母变成大写
#map(lambda, name) 就是把name列表中的元素经过函数计算放进map里
#list把map对象改编成列表
      
 
