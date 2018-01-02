import urllib.request
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8")
html1 = html[:299]
print(html1)
