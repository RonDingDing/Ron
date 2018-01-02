"""
In : import hashlib

In : hashlib.
hashlib.algorithms             #hashlib.sha1    ###这一列和md5都是一样的,只是算法不一样
hashlib.algorithms_available   #hashlib.sha224
hashlib.algorithms_guaranteed  #hashlib.sha256
#hashlib.md5                   #hashlib.sha384
hashlib.new                    #hashlib.sha512
hashlib.pbkdf2_hmac

In : a = hashlib.md5()

In : a.update("Sunny")   #往里面添加数据

In : a.update("Yes, ma'am")

In : a.digest()
Out: 'zdU\x97\x90\xbdv\x8a&\x03\x10\n\x8a|\xf8\xb0'

In : a.hexdigest()
Out: '7a64559790bd768a2603100a8a7cf8b0'   #查看XXXX

In : a.update("It's been a long time since he drinks")

In : a.hexdigest()
Out: '502b8046802eb4dddcf4ae6a2364d39c'






#####################################
In : import hashlib

In : a = hashlib.md5()

In : a.update("123456")

In : a.hexdigest()
Out: 'e10adc3949ba59abbe56e057f20f883e'

In : b = hashlib.md5()

In : b.update("123456")

In : b.hexdigest()
Out: 'e10adc3949ba59abbe56e057f20f883e'

###相同内容的加密是一样的



In : h.update("111")

In : h.hexdigest()
Out: '97f0e2f91b7e84b0d5e41011a3a373a1'
"""


"""
更吊的加密方式

In : import hmac

In : h = hmac.new("123456")

In : h.hexdigest()
Out: 'cab1380ea86d8acc9aa62390a58406aa'

In : h.update("111")

In : h.hexdigest()
Out: '97f0e2f91b7e84b0d5e41011a3a373a1'
"""
