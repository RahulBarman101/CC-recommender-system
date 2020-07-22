import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class recommend:
	def __init__(self):
		self.df = pd.read_csv('data.csv')
		self.features = self.df.iloc[:,2:].values
		self.features = list(self.features)
		# print(features.head())
		self.events = pickle.load(open('events.pickle','rb'))
		self.domains = pickle.load(open('domains.pickle','rb'))
		self.evs = []
		self.dom = None

		# s = input('Enter the sentence:')

	def predict(self,s,n):

		for j in self.domains.keys():
		    if j in s:
		    	z = self.domains[j.lower()]
		    	self.evs.append(z)
		    	self.dom = j

		for i in self.events.keys():
			if i in s:
				z = self.events[i.lower()]
				self.evs.append(z)

		
		# print(domains)
		# dom = input("enter the domain: ")
		# ev1 = input("enter event 1: ")
		# ev2 = input("enter event 2: ")

		# dom = domains[dom.lower()]

		# ev1 = events[ev1.lower()]
		# ev2 = events[ev2.lower()]



		# similar_metrics = cosine_similarity(features)

		result = np.where(self.features == self.evs)[0]
		print(result)
		print(self.evs)
		# print(len(result))
		# print(self.features[0])
		if len(result) == 0:
			# print(self.evs)
			self.features.append(self.evs)
			result = -1
			similar_metrics = cosine_similarity(self.features)
			result = list(enumerate(similar_metrics[result]))
			result = sorted(result,key= lambda x: x[1],reverse=True)
			return result
		else:
			similar_metrics = cosine_similarity(self.features)
			result = np.where(self.features == self.evs)[0][0]
			print(result)
			result = list(enumerate(similar_metrics[result]))
			result = sorted(result,key= lambda x: x[1],reverse=True)
			return result
