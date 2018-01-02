data = [1,23,45,223,46,43,35,85,43,22,3,56,7,8,99,2323]
count = 0
for j in range(1, len(data)):
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
        count +=1
    print(data)
print("count："count)
