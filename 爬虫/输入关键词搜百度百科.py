import urllib.request
import re
from bs4 import BeautifulSoup

keyword = input("请输入你要查找的关键词：")
keyword = urllib.parse.urlencode({"word":keyword})
url = "http://baike.baidu.com/search?word=" + keyword 
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser") # 使用 Python 默认的解析器
    
    
   

