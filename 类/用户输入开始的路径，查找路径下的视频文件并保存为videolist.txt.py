import os
def searchfile (startdir, target):
  os.chdir(startdir)

  for eachfile in os.listdir(os.curdir):
    extension = eachfile.splitext(eachfile)[1]
    if extension in target:
      videolist.append(os.getcwd() + os.sep + eachfile + os.linesep)
    if os.path.isdir(eachfile):
      searchfile(eachfile, target)
      os.chdir(os.pardir)

startdir = input("请输入待查找的初始目录：")
target = [".mp4", ".avi", ".rmvb"]
programdir = os.getcwd()
videolist = []

searchfile(startdir, target)

f = open(programdir + os.sep + "video.txt", "w")
f.writelines(videolist)
f.close()
