import time
import datetime

print("1", time.clock())                                        #返回处理器时间 3.3已经废弃
print("2", time.process_time())                                 #返回处理器时间，3.3已经废弃
print("3", time.time())                                         #返回当前系统时间戳1970年开始的
print("4", time.ctime())                                        #输出Sun May 21 22:02:40 2017

print("5", time.ctime(time.time()-86640))                       #将时间戳转为字符串格式
print("6", time.gmtime(time.time()-86640))                      #将时间戳转换成struct_time格式
print("7",time.localtime(time.time()-86640))                    #将时间戳转换成struct_time格式,但返回 的本地时间
print("8",time.mktime(time.localtime()))                        #与time.localtime()功能相反,将struct_time格式转回成时间戳格式
#time.sleep(4) #sleep
print("9",time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) )    #将struct_time格式转成指定的字符串格式
print("10",time.strptime("2016-01-28","%Y-%m-%d") )             #将字符串格式转换成struct_time格式
print("\n\n")
#datetime module

print("1",datetime.date.today())                                #输出格式 2016-01-26
print("2",datetime.date.fromtimestamp(time.time()-864400) )     #2016-01-16 将时间戳转成日期格式
current_time = datetime.datetime.now()
print("3",current_time)                                         #输出2016-01-26 19:04:30.335935
print("4",current_time.timetuple())                             #返回struct_time格式

#datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
print(current_time.replace(2014,9,12))                          #输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10)#比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10)#比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120)#比现在+120s
print(new_date)
