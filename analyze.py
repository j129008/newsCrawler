import pickle

data = []
with open("./newsData.pkl", 'rb') as fr:
    data = pickle.load(fr)
print(data)
