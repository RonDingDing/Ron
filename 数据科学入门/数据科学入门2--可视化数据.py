#! /usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

# # 线形图
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# 创建一幅线图， x轴是年份， y轴是gdp
plt.plot(years, gdp, color='red', marker='o', linestyle='solid')
# 添加一个标题
plt.title('Gdp')
# 给y轴加标记
plt.ylabel('billions')
plt.show()
# plt.savefig()



# ##########################################################
# 条形图
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 条形的默认宽度是0.8， 因此我们对左侧坐标加上0.1
# 这样每个条形就被放置在中心了
xs = [i + 0.1 for i, _ in enumerate(movies)]

# 使用左侧x坐标[xs]和高度[num_oscars]画条形图
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# 使用电影的名字标记x轴， 位置在x轴上条形的中心
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()

############################################
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10

from collections import Counter

histogram = Counter(decile(grade) for grade in grades)
print(histogram)
plt.bar([x - 4 for x in histogram.keys()],  # 每个条形向左侧移动4个单位
        histogram.values(),  # 给每个条形设置正确的高度
        8)  # 每个条形的宽度设置为8
plt.axis([-10, 105, 0, 5])
# x轴取值从-5到105
# y轴取值0到5
plt.xticks([10 * i for i in range(11)])  # x轴标记为0， 10， ...， 100
plt.xlabel("Decile")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

##################################################
#线形图2
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# 可以多次调用plt.plot
# 以便在同一个图上显示多个序列
plt.plot(xs, variance,     'g-',  label='Variance')  # 绿色实线
plt.plot(xs, bias_squared, 'r-.', label='Bias^2')  # 红色点虚线
plt.plot(xs, total_error,  'b:',  label='Total Error')  # 蓝色点线
# 因为已经对每个序列都指派了标记
# 所以可以自由地布置图例
# loc=9指的是 “顶部中央”
plt.legend(loc=9)
plt.xlabel('Model Complexity')
plt.title('The Bias-Variance Tradeoff')
plt.show()

###################################################

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# 每个点加标记
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),  # 把标记放在对应的点上
                 xytext=(5, -5),                   # 但要有轻微偏离
                 textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("Number of friends")
plt.ylabel('Daily minutes spent on the site')
plt.show()