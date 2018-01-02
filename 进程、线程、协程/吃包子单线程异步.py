import time
def consumer(name):
    while True:
        print('【%s】准备吃包子啦' % name)
        while True:
            baozi = yield
            print("包子【%s】来了，被【%s】吃了！" % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__() #只是为了打印“准备吃包子”
    c2.__next__()#只是为了打印“准备吃包子”

    print("【%s】开始做包子啦！" % name)
    for i in range(10):
        time.sleep(1)
        print("做了两个包子！")
        c.send(i)  #把做好的包子交到baozi那里
        c2.send(i)


producer('ron')
