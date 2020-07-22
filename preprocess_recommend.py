import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('CCMLEmployeeData.csv')
df['Domain'] = df['Domain'].str.lower()
df['Event1'] = df['Event1'].str.lower()
df['Event2'] = df['Event2'].str.lower()
# print(df.head())

events = np.unique(df['Event1'].values)
evs = {}
for idx,i in enumerate(events):
	evs[i[:-1]] = idx

df['Event1'] = df['Event1'].map(evs)
df['Event2'] = df['Event2'].map(evs)

pickle.dump(evs,open('events.pickle','wb+'))

doms = np.unique(df['Domain'].values)
domain = {}

for idx,i in enumerate(doms):
	domain[i[:-1]] = idx

df['Domain'] = df['Domain'].map(domain)
pickle.dump(domain,open('domains.pickle','wb+'))
# print(df['Domain'].head())
df.to_csv('data.csv')
