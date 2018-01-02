What is redis?

Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

Redis官网：http://redis.io/

以上摘自官网介绍
安装Redis

安装

模块GitHub地址：https://github.com/WoLpH/redis-py

Shell

[root@anshengme ~]# yum -y install redis
1
[root@anshengme ~]# yum -y install redis
配置绑定的IP

Shell

[root@anshengme ~]# vim /etc/redis.conf 
bind 0.0.0.0
1
2
[root@anshengme ~]# vim /etc/redis.conf 
bind 0.0.0.0
启动并设置开机自启动

Shell

[root@anshengme ~]# systemctl start redis
[root@anshengme ~]# systemctl enable redis
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
1
2
3
[root@anshengme ~]# systemctl start redis
[root@anshengme ~]# systemctl enable redis
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
检查

查看端口

Shell

[root@anshengme ~]# netstat -tlnp | grep "redis"
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1439/redis-server 0
1
2
[root@anshengme ~]# netstat -tlnp | grep "redis"
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1439/redis-server 0
数据写入测试

Shell

[root@anshengme ~]# /usr/bin/redis-cli 
127.0.0.1:6379> set url https://blog.ansheng.me
OK
127.0.0.1:6379> get url
"https://blog.ansheng.me"
127.0.0.1:6379> exit
1
2
3
4
5
6
[root@anshengme ~]# /usr/bin/redis-cli 
127.0.0.1:6379> set url https://blog.ansheng.me
OK
127.0.0.1:6379> get url
"https://blog.ansheng.me"
127.0.0.1:6379> exit
安装redis-py

安装redis-py

Shell

pip3 install redis
1
pip3 install redis
或源码安装

Shell

python setup.py install
1
python setup.py install
检查安装是否成功

Python

# 导入模块没报错则安装成功
>>> import redis
1
2
# 导入模块没报错则安装成功
>>> import redis
入门及使用

Python

# 导入模块
>>> import redis
# 连接到Redis服务器
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# 写入一条数据
>>> conn.set('name','ansheng')
True
# 获取一条数据
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
1
2
3
4
5
6
7
8
9
10
11
12
# 导入模块
>>> import redis
# 连接到Redis服务器
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# 写入一条数据
>>> conn.set('name','ansheng')
True
# 获取一条数据
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
使用连接池连接到Redis

Behind the scenes, redis-py uses a connection pool to manage connections to a Redis server. By default, each Redis instance you create will in turn create its own connection pool. You can override this behavior and use an existing connection pool by passing an already created connection pool instance to the connection_pool argument of the Redis class. You may choose to do this in order to implement client side sharding or have finer grain control of how connections are managed.
Python

>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
1
2
3
4
5
6
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
使用套接字连接

Python

>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
1
>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
API

redis-py提供的API用来操作redis

String API

set(name, value, ex=None, px=None, nx=False, xx=False)

参数	描述
ex	过期时间（秒）
px	过期时间（毫秒）
nx	如果设置为True，则只有name不存在时，当前set操作才执行
xx	如果设置为True，则只有name存在时，岗前set操作才执行
Python

>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
1
2
3
4
5
>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
setex(name, value, time)

设置过期时间/秒

Python

>>> conn.setex('k','v',1)
True
>>> conn.get('k')
1
2
3
>>> conn.setex('k','v',1)
True
>>> conn.get('k')
psetex(name, time_ms, value)

设置过期时间/毫秒

Python

>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
1
2
3
>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
setnx(name, value)

设置值，只有key不存在时，执行设置操作

Python

>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
1
2
3
4
5
6
7
>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
mset(*args, **kwargs)

同时设置多个key/value

Python

>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
1
2
3
4
>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
get(name)

获取单个值

Python

>>> conn.get('k1')
b'v1'
1
2
>>> conn.get('k1')
b'v1'
mget(keys, *args)

获取多个值

Python

>>> conn.mget('k1','k2')
[b'v1', b'v2']
# 传入列表
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
1
2
3
4
5
>>> conn.mget('k1','k2')
[b'v1', b'v2']
# 传入列表
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
getset(name, value)

设置新值并获取原来的值

Python

>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
1
2
3
4
5
6
7
>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
getrange(key, start, end)

通过索引的方式来获取value的值

Python

>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
1
2
3
4
>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
setrange(name, offset, value)

根据索引修改value

Python

>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
1
2
3
4
5
6
>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
setbit(name, offset, value)

getbit(name, offset)

获取value对应某一个索引位置对应的值0/1

Python

>>> conn.getbit('k',1)
1
1
2
>>> conn.getbit('k',1)
1
bitcount(key, start=None, end=None)

获取key对应二进制中表示1的个数

bitop(operation, dest, *keys)

将多个值进行值运算，得出的结果保存到一个新值当中

Python

>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
1
2
3
4
5
6
7
8
>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
operation支持AND(并)、OR(或)、NOT(非)、XOR(异或)
strlen(name)

获取value的长度

Python

>>> conn.set('name','安生')
True
>>> conn.strlen('name')
6
1
2
3
4
>>> conn.set('name','安生')
True
>>> conn.strlen('name')
6
incr(name, amount=1)

对name的value进行自增，如果name不存在则创建，否则自增

Python

>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
1
2
3
4
5
6
7
8
9
>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
incrbyfloat(name, amount=1.0)

同上，支持浮点数自增

Python

>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
1
2
3
4
>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
decr(name, amount=1)

自减，同自增一样，如果进行自减的value不是整数就报错

Python

>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
1
2
3
4
5
6
>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
append(key, value)

在value后面追加内容

Python

>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
1
2
3
4
5
6
>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
Hash API

hset(name, key, value)

设置name的键值对，有则修改，没有则创建

Python

>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
1
2
3
4
>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
hmset(name, mapping)

同时设置多个name的key/value

Python

>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
1
2
3
4
>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
hget(name, key)

获取name中key的值

Python

>>> conn.hget('dic','k2')
b'v2'
1
2
>>> conn.hget('dic','k2')
b'v2'
hmget(name, keys, *args)

同时获取多个

Python

>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
1
2
3
4
>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
hgetall(name)

获取name对应的所有key/value

Python

>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
1
2
>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
hlen(name)

获取name对应键值对的个数

Python

>>> conn.hlen('dic')
2
1
2
>>> conn.hlen('dic')
2
hkeys(name)

获取name中所有的key

Python

>>> conn.hkeys('dic')
[b'k1', b'k2']
1
2
>>> conn.hkeys('dic')
[b'k1', b'k2']
hvals(name)

获取name中所有的value

Python

>>> conn.hvals('dic')
[b'v1', b'v2']
1
2
>>> conn.hvals('dic')
[b'v1', b'v2']
hexists(name, key)

检查当前name中是否有传入的key

Python

>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
1
2
3
4
>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
hdel(self, name, *keys)

删除name中对应的key

Python

>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
1
2
3
>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
hincrby(name, key, amount=1)

name中key对应的value进行自增，如果不存在则创建

Python

>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
1
2
3
4
>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
hincrbyfloat(name, key, amount=1.0)

value自增，支持浮点数，同上

Python

>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
1
2
3
4
>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
hscan(name, cursor=0, match=None, count=None)

增量式迭代获取，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆

参数	描述
name	redis的name
cursor	游标（基于游标分批取获取数据）
match	匹配指定key，默认None 表示所有的key
count	每次分片最少获取个数，默认None表示采用Redis的默认分片个数
hscan_iter(name, match=None, count=None)

利用yield封装hscan创建生成器，实现分批去redis中获取数据

参数	描述
match	匹配指定key，默认None 表示所有的key
count	每次分片最少获取个数，默认None表示采用Redis的默认分片个数
如：

Python

for item in r.hscan_iter('xx'):
    print item
1
2
for item in r.hscan_iter('xx'):
    print item
expire(name, time)

设置过期时间

Python

>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
1
2
3
4
5
6
7
>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
ListAPI

lpush(name, *values)

在最左边添加值

Python

>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
1
2
3
4
>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
rpush(name, *values)

在最右边添加值

Python

>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
1
2
3
4
>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
lpushx(name, value)

只有name已经存在时，值添加到列表的最左边

Python

>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
1
2
3
4
>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
rpushx(name, value)

只有name已经存在时，值添加到列表的最右边

Python

>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
1
2
3
4
5
6
>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
llen(name)

获取name元素的个数

Python

>>> conn.llen('li')
5
1
2
>>> conn.llen('li')
5
linsert(name, where, refvalue, value)

在name的某一个值前面或者后面插入一个新值

Python

>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
1
2
3
4
5
6
>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
lset(name, index, value)

对name中index索引位置的值进行重新赋值

Python

>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
1
2
3
4
5
6
>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
lrem(name, value, num=0)

删除指定value后面或者前面的值

num=2,从前到后，删除2个；
num=-2,从后向前，删除2个
Python

>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
1
2
3
4
5
6
7
8
9
10
>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
lpop(name)

删除name中左侧第一个元素

Python

>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
1
2
3
4
>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
rpop(name)

删除name中右侧第一个元素

Python

>>> conn.rpop('li')
b'33'
1
2
>>> conn.rpop('li')
b'33'
lindex(name, index)

获取name中对应索引的值

Python

>>> conn.lindex('li', 0)
b'aa'
1
2
>>> conn.lindex('li', 0)
b'aa'
lrange(name, start, end)

使用切片获取数据

Python

>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
1
2
3
4
>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
ltrim(name, start, end)

在name对应的列表中移除没有在start-end索引之间的值

Python

>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
1
2
3
4
>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
rpoplpush(src, dst)

从src列表中取出最右边的元素，同时将其添加至dst列表的最左边

Python

>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
1
2
3
4
5
6
>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
blpop(keys, timeout=0)
brpop(keys, timeout=0)

brpoplpush(src, dst, timeout=0)

从src列表的右侧移除一个元素并将其添加到dst列表的左侧

Python

>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
1
2
3
4
5
6
>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
自定义增量迭代

由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：

获取name对应的所有列表
循环列表
但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

Python

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
1
2
3
4
5
6
7
8
9
def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
使用

Python

for item in list_iter('pp'):
    print item
1
2
for item in list_iter('pp'):
    print item
SET API

sadd(name, *values)

为name添加值，如果存在则不添加

Python

>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
1
2
3
4
>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
scard(name)

返回name的元素数量

Python

>>> conn.scard('s1')
1
1
2
>>> conn.scard('s1')
1
sdiff(keys, *args)

在keys集合中不在其他集合中的数据

Python

>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
1
2
>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
sdiffstore(dest, keys, *args)

在keys集合中不在其他集合中的数据保存到dest集合中

Python

>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
1
2
3
4
>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
sinter(keys, *args)

获取keys集合中与其他集合中的并集

Python

>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
1
2
>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
sinterstore(dest, keys, *args)

获取keys集合中与其他集合中的并集数据并保存到dest集合中

Python

>>> conn.sinterstore('news1','s1','s2')
3
1
2
>>> conn.sinterstore('news1','s1','s2')
3
sismember(name, value)

获取value是否是name集合中的成员

Python

>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
1
2
3
4
>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
smembers(name)

获取name集合中所有的成员

Python

>>> conn.smembers('news1')
{b'2', b'3', b'1'}
1
2
>>> conn.smembers('news1')
{b'2', b'3', b'1'}
smove(src, dst, value)

将src中的value移动到dst中

Python

>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
spop(name)

删除并返回name中的随机成员

Python

>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
srandmember(name, number=None)

随机获取name集合中的number个成员，默认number=1

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
srem(name, *values)

删除name集合中的values数据

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
1
2
3
4
5
6
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
sunion(keys, *args)

获取keys集合与其他集合的并集

Python

>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
5
6
>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
sunionstore(dest, keys, *args)

获取keys集合与其他集合的并集并保存到dest中

Python

>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
Ordered set API

zadd(name, *args, **kwargs)

Python

>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
1
2
3
4
>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
zcard(name)

返回有序集合name元素的数量

Python

>>> conn.zcard('h1')
2
1
2
>>> conn.zcard('h1')
2
zcount(name, min, max)

返回在name中值在min与max之间的值个数

Python

>>> conn.zcount('h1',10,30)
2
1
2
>>> conn.zcount('h1',10,30)
2
zincrby(name, value, amount=1)

name中让value的值加上amount

Python

>>> conn.zincrby('h1','n1',10)
21.0
1
2
>>> conn.zincrby('h1','n1',10)
21.0
zinterstore(dest, keys, aggregate=None)
zlexcount(name, min, max)

zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)

参数	描述
name	redis的name
start	有序集合索引起始位置（非分数）
end	有序集合索引结束位置（非分数）
desc	排序规则，默认按照分数从小到大排序
withscores	是否获取元素的分数，默认只获取元素的值
score_cast_func	对分数进行数据转换的函数
Python

>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
1
2
3
4
>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
Python

# 从大到小排序
zrevrange(name, start, end, withscores=False, score_cast_func=float) 
# 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# 从大到小排序
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
1
2
3
4
5
6
# 从大到小排序
zrevrange(name, start, end, withscores=False, score_cast_func=float) 
# 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# 从大到小排序
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
zrangebylex(name, min, max, start=None, num=None)

当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员

对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大

参数	描述
name	redis的name
min	左区间(值) + 表示正无限； – 表示负无限； ( 表示开区间； [ 则表示闭区间
min	右区间（值）
start	对结果进行分片处理，索引位置
num	对结果进行分片处理，索引后面的num个元素
如：

Python

ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
1
2
ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
更多：

Python

# 从大到小排序
zrevrangebylex(name, max, min, start=None, num=None)
1
2
# 从大到小排序
zrevrangebylex(name, max, min, start=None, num=None)
zrevrangebylex(name, max, min, start=None, num=None)

zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)**

zrank(name, value)

返回基于0的值，指示在排序集名称的值排名

Python

>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
1
2
3
4
>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
zrevrank(name, value)，从大到小排序
zrem(name, *values)

删除name中对应的values

Python

>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
1
2
3
4
>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
zremrangebyrank(name, min, max)

根据排行范围进行删除

Python

>>> conn.zremrangebyrank('h1',1,2)
1
1
2
>>> conn.zremrangebyrank('h1',1,2)
1
zremrangebyscore(name, min, max)

根据分数范围进行删除

Python

>>> conn.zremrangebyscore('h1',10,20)
2
1
2
>>> conn.zremrangebyscore('h1',10,20)
2
zscore(name, value)

返回指定value的值是多少

Python

>>> conn.zscore('h1','n1')
11.0
1
2
>>> conn.zscore('h1','n1')
11.0
zunionstore(dest, keys, aggregate=None)

Global API

delete(*names)

在redis中删除names

Python

>>> conn.delete('ooo')
1
1
2
>>> conn.delete('ooo')
1
exists(name)

检测name是否存在

Python

>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
1
2
3
4
>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
keys(pattern=’*’)

Python

# 匹配数据库中所有 key 
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
1
2
3
# 匹配数据库中所有 key 
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
Python

# 匹配hello，hallo和hxllo等
conn.keys(pattern='h?llo')
# 匹配hllo和heeeeello 等
conn.keys(pattern='h*llo')
# 匹配hello和hallo，但不匹配 hillo
conn.keys(pattern='h[ae]llo')
1
2
3
4
5
6
# 匹配hello，hallo和hxllo等
conn.keys(pattern='h?llo')
# 匹配hllo和heeeeello 等
conn.keys(pattern='h*llo')
# 匹配hello和hallo，但不匹配 hillo
conn.keys(pattern='h[ae]llo')
rename(src, dst)

把src重命名成dst

Python

>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
1
2
3
4
5
6
7
8
9
>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
move(name, db)

将redis的某个值移动到指定的db下

randomkey()

随机获取一个redis的name，不进行删除

Python

>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
1
2
3
4
>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
type(name)

查看name的类型

Python

>>> conn.type('kk')
b'string'
1
2
>>> conn.type('kk')
b'string'
管道

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作(MySQL中的事务)。

Python

>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# 创建一个通道支持事务
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# 如果在设置上面两个值的过程中出错了，那么这次提交就不会执行
>>> pipe.execute()
[]
1
2
3
4
5
6
7
8
9
10
11
12
13
>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# 创建一个通道支持事务
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# 如果在设置上面两个值的过程中出错了，那么这次提交就不会执行
>>> pipe.execute()
[]
发布订阅

Python

# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py 订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py 发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py 订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py 发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
