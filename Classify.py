import splitt
import numpy as np

class Classifier:

	def __init__(self,splitFunction):
		self.splitFunction = splitFunction
		#self.fCount = {}
		try:
			self.fCount = np.load("fCountdict.npy").item()
		except IOError:
			self.fCount = {}

		#self.catCount= {}
		try:
			self.catCount = np.load("catCountdict.npy").item()
		except IOError:
			self.catCount = {}

	def incfCount(self,feature,category):
		self.fCount.setdefault(feature,{})
		self.fCount[feature].setdefault(category,0)
		self.fCount[feature][category] += 1


	def incCatCount(self,category):
		self.catCount.setdefault(category,0)
		self.catCount[category] += 1

	def getFCCount(self,feature,category):
		if feature in self.fCount and category in self.fCount[feature]:
			return float(self.fCount[feature][category])
		return 0.0

	def getCatCount(self,category):
		if category in self.catCount:
			return float(self.catCount[category])
		return 0.0
	def totalCount(self):
		temp = self.catCount.values()
		if len(temp)!=0:

			return float(sum(temp))
		else:
			return 0.0
	def categories(self):
		temp = self.catCount.keys()
		return temp

	def train(self,element,category):
		features = self.splitFunction(element)
		for temp in features:
			self.incfCount(temp,category)
		self.incCatCount(category)

	def probFgC(self,feature,category):
		# P(feature|category)
		if self.getCatCount(category) == 0:
			return 0.0
		return self.getFCCount(feature,category)/self.getCatCount(category)

	def weightavgFgC(self,feature,category,weight=1,assumed=0.5):
		prob = self.probFgC(feature,category)
		l = self.categories()
		#print l
		s = 0.0
		for t in l:
			s += self.getFCCount(feature,t)
		result = (weight * assumed) + (s * prob)
		result /= (weight + s)
		#print("ppp\n%d\n"%result)
		return result
	def saveDict(self):
		np.save('fCountdict.npy',self.fCount)
		np.save('catCountdict.npy',self.catCount)
