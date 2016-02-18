import urllib.request
from bs4 import BeautifulSoup

data = []
url = 'http://newtalk.tw/news/view/2008-08-28/'

post = []
fp = urllib.request.urlopen(url+str(2))
soup = BeautifulSoup(fp , 'html.parser')

title = soup.select('.content_title')[0].string
post.append(title)

content = ''
lineList = soup.txt.find_all('p')
for line in lineList:
    lineStr = line.string
    if (lineStr != None) and ("連結" not in lineStr):
        content += lineStr
post.append(content)
data.append(post)
print(data)
