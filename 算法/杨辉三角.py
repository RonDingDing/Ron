def yanghui(num):
    def triangle():
        li = [1]     
        while True:
            yield li    
            li = [1] + [li[i]+li[i+1] for i in range(len(li) - 1) ] + [1]
    o = triangle()
    for i in range(num):
        print(next(o))

      
 
