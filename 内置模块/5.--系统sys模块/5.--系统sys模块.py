import sys
sys.argv        #命令行参数List，第一个元素是程序本身路径
sys.exit(n)     #打印括号中的字符串，退出程序
sys.version     #获取python解析程序的版本信息
sys.path        #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的路径
sys.platform    #返回操作系统平台名称
sys.stdout.write("Please:") #标准输出
sys.stdin.readline()[:-1]   #输入一行之后获取这一行（删掉换行符\n）
