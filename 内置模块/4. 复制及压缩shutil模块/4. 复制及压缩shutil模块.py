import shutil

shutil.copyfileobj(fsrc, fdst,[,length]) #将文件内容拷贝到另一个文件中，可以部分内容
shutil.copyfile(src, dst)                #拷贝文件
shutil.copymode(src, dst)                #仅拷贝权限，内容、组、用户均不变
shutil.copystat(src, dst)                #拷贝状态的信息，包括mode bits, atime, mtime, flags
shutil.copy(src, dst)                    #拷贝文件和权限
shutil.copy2(src, dst)                   #拷贝文件和状态信息
shutil.ignore_patterns(*patterns)
shutil.copytree(src, des, symlinks=False, ignore=None)
                                         #递归地拷贝文件
shutil.rmtree(path[,ignore_errors[, onerror]])
                                         #递归地删除文件
shutil.move(src, dst)                    #递归地移动文件
shutil.make_archive(base_name, format, ... ) #创建压缩包并返回文件路径
#base_name：压缩包的文件名，也可以是压缩包的路径，只是文件名时，则保存至当前目录，否则保存至指定路径
#format: 压缩包种类，zip/tar/bztar/gztar
#root_dir:要压缩的文件夹路径（默认当前目录）
#owner:用户，默认当前用户
#group:组，默认当前组
#logger：用于记录日志，通常是logginglogger对象


import zipfile

#压缩
z = zipfile.ZipFile("laxi.zip", 'w')#打开文件
z.write('a.log')
z.write('data.data')
z.close()

#解压
z = zipfile.ZipFile("laxi.zip", 'r')
z.extractall()
z.close()


import tarfile

#压缩
tar = tarfile.open('your.tar', 'w')
tar.add('/Users/wupeqi/Pycharm.zip', arcname='bbs2.zip')
tar.add('/Users/wupeqi/Pycharm1.zip', arcname='bb22.zip')
tar.close()

#解压
tar = tarfile.open('your.tar', 'r')
tar.extractall() #可设置解压地址
tar.close()
