import pickle
import opencc

data = []
with open("./newsData.pkl", 'rb') as fr:
    data = pickle.load(fr)
dataCn = []
for post in data:
    postCn = []
    for ele in post:
        postCn.append(opencc.convert(ele))
    dataCn.append(postCn)

with open("./newsDataCn.pkl", 'wb') as fw:
    pickle.dump(dataCn, fw)
