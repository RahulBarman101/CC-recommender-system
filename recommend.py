import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('data.csv')
features = df.iloc[:,2:]

# print(features.head())
events = pickle.load(open('events.pickle','rb'))
domains = pickle.load(open('domains.pickle','rb'))
# print(domains)
dom = input("enter the domain: ")
ev1 = input("enter event 1: ")
ev2 = input("enter event 2: ")

dom = domains[dom.lower()]

ev1 = events[ev1.lower()]
ev2 = events[ev2.lower()]

similar_metrics = cosine_similarity(features)

result = np.where(features == [dom,ev1,ev2])[0][0]

result = list(enumerate(similar_metrics[result]))
result = sorted(result,key= lambda x: x[1],reverse=True)
top_5 = result[:5]

for i in top_5:
	print(df['Name'].iloc[i[0]])
