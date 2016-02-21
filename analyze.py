import pickle
import jieba
import jieba.analyse
import operator

data = []
with open("./newsDataCn.pkl", 'rb') as fr:
    data = pickle.load(fr)

allTag = []
for i in range(1, 100):
    allTag += jieba.analyse.extract_tags(data[i][1],topK=3)

d = {}
for ele in allTag:
    try:
        d[ele] += 1
    except:
        d[ele] = 1

d = sorted(d.items(), key=operator.itemgetter(1))

for ele in d:
    print(ele[0])
