def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        # 上面这行去掉就是7.13
        count += 1
        total += new_value
        return total / count

    return averager


a = make_averager()
a(3)
print(a(4))
