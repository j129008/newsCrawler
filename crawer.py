import urllib.request
from bs4 import BeautifulSoup
import pickle
import sys
import requests

data = []
url = 'http://newtalk.tw/news/view/2008-08-28/'
fbAPI = 'http://api.facebook.com/restserver.php?method=links.getStats&urls='
start = int(sys.argv[1])
end = int(sys.argv[2])
for i in range(start,end+1):
    print(str(i)+'/'+str(end))
    post = []
    urlGet = requests.get(url+str(i))
    fp = urllib.request.urlopen(urlGet.url)
    fp_fbAPI = urllib.request.urlopen(fbAPI+urlGet.url)
    soup = BeautifulSoup(fp , 'html.parser')
    soup_fb = BeautifulSoup(fp_fbAPI , 'html.parser')
    try:
        title = soup.select('.content_title')[0].string
        author = soup.select('.content_reporter')[0].a.string
        likes = soup_fb.total_count.string
        post.append(str(title))
        post.append(str(author))
        post.append(str(likes))
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
