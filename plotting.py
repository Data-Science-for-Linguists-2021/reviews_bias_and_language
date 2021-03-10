import json
import pandas as pd
import nltk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

def isRes(ID):
        if ID in res_tag:
                return True
        else:
                return False

f = open('business.pkl', 'rb')
res_tag = pickle.load(f)
f.close()


# Reviews

fn = 'C:\Spring2021\data_science\project\yelp_dataset\yelp_academic_dataset_review.json'
ChunkSize = 100000


for chunk in pd.read_json(fn, chunksize=ChunkSize, lines=True):
	print(chunk.shape)
	print(chunk.head())
	break

# sort out restaurants from other businesses
chunk['is_res'] = chunk['business_id'].map(lambda x: isRes(x))
chunk = chunk[chunk['is_res'] == True]

# making str number ints
chunk['stars'] = chunk['stars'].map(lambda x: int(x))

# tokenizing
chunk['sents'] = chunk['text'].map(lambda x: nltk.sent_tokenize(x))
np.corrcoef(chunk['stars'], chunk['useful'])
#sns.scatterplot(x=chunk['stars'], y=chunk['useful'])
plt.show()

# have to run to_csv from the idle

sent1 = []

for i in chunk['review_id'][:1000]:
	sent1.append([i, list(chunk[chunk['review_id'] == i]['sents'])])

sent1 = [[x, y[0]] for [x,y] in sent1]

sent2 = []

for i in sent1:
	counter = 1
	for x in i[1]:
		sent2.append([i[0], counter, x])
		counter = counter + 1

sentfd = pd.DataFrame(sent2)
sentfd.to_csv('sents.csv')
