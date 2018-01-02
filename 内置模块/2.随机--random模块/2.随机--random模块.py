#常用的有这几个

random.randrange(stop)
random.randrange(start, stop[, step])

    #从range(start, stop, step)返回一个start到end范围内的随机整数（译者注：start，end，step都是整数，不包含end），可以指定step。这等同于选择（范围（开始， 停止， 步骤）） 范围对象。
    #位置参数模式与range()匹配。不应使用关键字参数，因为函数可能以意想不到的方式使用它们。
    #在版本3.2中更改： randrange()更复杂地生成平均分布的值。以前，它使用类似int(random()*n)这样可能产生轻微的不均匀分布。
random.randint(a, b)
    #返回随机整数N以使得a N / t5> b。 randrange（a， b + 1）的别名。

#序列函数：

random.choice(seq)
    #从非空序列seq返回一个随机元素。如果seq为空，则引发IndexError。
random.shuffle(x[, random])
    #随机播放序列x。可选参数random是返回[0.0，1.0）中的随机浮点的0参数函数；默认情况下，这是函数random()。
    #注意，对于甚至相当小的len(x)，x的排列的总数大于大多数随机数生成器的周期；这意味着长序列的大多数排列永远不会生成。

random.sample(population, k)

    #返回从群体序列或集合中选择的唯一元素的k长度列表。用于随机抽样，无需更换。
    #返回包含来自总体的元素的新列表，而保持原始填充值不变。结果列表以选择顺序，使得所有子片段也将是有效的随机样本。这允许抽奖获奖者（样本）被分成大奖和第二名获奖者（子分类）。
    #群体的成员不需要hashable或唯一的。如果群体包含重复，则每次出现是样品中的可能选择。
    #要从整数范围中选择样本，请使用range()对象作为参数。这对于从大群体采样是特别快速和节省空间的：样本（范围（10000000）， 60）。
    #如果样本大小大于总体大小，则会引发ValueError。

#以下函数生成特定的实值分布。函数参数以分布方程中的相应变量命名，如在常见的数学实践中使用的；大多数这些方程可以在任何统计文本中找到。

random.random()
    #返回下一个在范围 [0.0, 1.0) 中的随机浮点数。
