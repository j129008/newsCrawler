import pickle

data = []
with open("./newsDataCn.pkl", 'rb') as fr:
    data = pickle.load(fr)
