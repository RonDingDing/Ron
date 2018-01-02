import urllib.request
import re
from bs4 import BeautifulSoup


url = "http://www.douban.com"
request = urllib.request.urlopen(url)
html = request.read()
soup = BeautifulSoup(html, "html.parser")

linklist = []
for each in soup.find_all(href = re.compile("")):                       #寻找soup中的所有包括view的东西
     label = each.text + "-->"+each["href"]     #each.text 是标题内容    each["href"]是连接内容
     linklist.append(label)
 
linklist = list(set(linklist))                                              #剔除重复内容

for eaach in linklist:
     print(eaach)

