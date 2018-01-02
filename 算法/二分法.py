def binarySearch(dataSource, findN):
    mid = int(len(dataSource)/2)
    if len(dataSource) >= 1:
    
        if dataSource[mid] > findN: #数据在左边
            print("data in left of [%s]" % dataSource[mid])
            print(dataSource[:mid], "\n")
            binarySearch(dataSource[:mid], findN)
            
        elif dataSource[mid] < findN: #数据在右边            
            print("data in right of [%s]" % dataSource[mid])
            print(dataSource[mid:], "\n")
            binarySearch(dataSource[mid:], findN)

        else:
            print("found findN, ", dataSource[mid])
            
    else:
        print("cannot find..")

        
        

data = list(range(1, 60, 3))
binarySearch(data, 39)


