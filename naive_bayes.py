'''
Naive bayes classifier written in python 
'''
from __future__ import division
import math
import operator
from preprocessor import preprocess

class NaiveBayesClassifier(object):
	def __init__(self,file=None):
		self.training_data = {} # dictionary to store all information related to training data
		self.training_data['labels'] = {}
		self.training_data['total_data_set'] = 0
		
	
	def train(self,text,label):
		data = preprocess(text)
		self.training_data['total_data_set']+=1
		
		if label in self.training_data['labels']:
			self.training_data['labels'][label]['docs']+=1
			
		else :
			self.training_data['labels'][label] = {}
			self.training_data['labels'][label]['docs'] = 1
			self.training_data['labels'][label]['keywords'] = {}
			self.training_data['labels'][label]['total_keywords'] = 0
			

		for word in data :
			self.training_data['labels'][label]['total_keywords']+=1
			if word in self.training_data['labels'][label]:
				self.training_data['labels'][label]['keywords'][word]+=1				
			else:
				self.training_data['labels'][label]['keywords'][word]=1

		#print self.training_data



	def classify(self,text):
		data = preprocess(text)
		label_weights = {}
		for label in self.training_data['labels']:

			prior = math.log10(1+(self.training_data['labels'][label]['docs'])/(self.training_data['total_data_set']))
			term_weight = 0
			for word in data:
				if word in self.training_data['labels'][label]['keywords']:
					n = self.training_data['labels'][label]['keywords'][word]
				else :
					n = 0
				
				term_weight+= math.log10((n+1)/(self.training_data['labels'][label]['docs']+ len(data)))

			label_weights[label] = prior + term_weight

		
		return max(label_weights.iteritems(), key=operator.itemgetter(1))[0]



clss = NaiveBayesClassifier()
clss.train('AAP releases manifestos for 28 Assembly constituencies','politics')
clss.train('FIRs filed against UP sugar mill owners','law')
clss.train('BJP will win in four states due to anti-Congress wave: Arun Jaitley','politics')
clss.train('AAP trashes BJP charge of playing religious card','politics')
print clss.classify('BJP has become a party by Modi, for Modi, of Modi: Congress')



