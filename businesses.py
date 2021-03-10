import json
import pandas as pd
import nltk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def isRes(cat):
	if 'Restaurants' in nltk.word_tokenize(str(cat)):
		return True
	else:
		return False

fn = 'C:\Spring2021\data_science\project\yelp_dataset\yelp_academic_dataset_business.json'
for chunk in pd.read_json(fn, chunksize=500000, lines=True):
	print(chunk.shape)
	print(chunk.head())
	break

chunk['restaurant'] = chunk['categories'].map(lambda x: isRes(x))
