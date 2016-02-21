import pickle
# import jieba
# import jieba.analyse
# import operator

data = []
with open("./newsDataCn.pkl", 'rb') as fr:
    data = pickle.load(fr)

likes = dict()
posts = dict()
for i in range(len(data)):
    authors = data[i][1].split("、")
    likesCnt = data[i][2]
    for author in authors:
        try:
            likes[author] += int(likesCnt)
            posts[author] += 1
        except:
            likes[author] = int(likesCnt)
            posts[author] = 1

for author in likes:
    print( author + ' ' + str(likes[author]/posts[author]) )
# allTag = []
# for i in range(1, len(data)):
    # allTag += jieba.analyse.extract_tags(data[i][1],topK=3)

# d = {}
# for ele in allTag:
    # try:
        # d[ele] += 1
    # except:
        # d[ele] = 1

# d = sorted(d.items(), key=operator.itemgetter(1))

# for ele in d:
    # print(ele[0])
