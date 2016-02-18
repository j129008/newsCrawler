import urllib.request
from bs4 import BeautifulSoup
import pickle
import sys

data = []
url = 'http://newtalk.tw/news/view/2008-08-28/'
start = int(sys.argv[1])
end = int(sys.argv[2])
for i in range(start,end+1):
    print(str(i)+'/'+str(end))
    post = []
    fp = urllib.request.urlopen(url+str(i))
    soup = BeautifulSoup(fp , 'html.parser')
    try:
        title = soup.select('.content_title')[0].string
        post.append(str(title))
    except:
        print('404')
        continue

    content = ''
    lineList = soup.txt.find_all('p')
    for line in lineList:
        lineStr = line.string
        if (lineStr != None) and ("連結" not in lineStr):
            content += lineStr.replace('\u3000','')
    post.append(str(content))
    data.append(post)

with open('newsData.pkl','wb') as fs:
    pickle.dump(data, fs)
