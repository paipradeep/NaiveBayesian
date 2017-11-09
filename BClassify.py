from Classify import Classifier
class BayesianClassifier(Classifier):

	def elementProbability(self,element,category):

		features = self.splitFunction(element)
		result = 1
		for f in features:
			result *= self.weightavgFgC(f,category)
		#print result
		return result

	def Final(self,element,category):
		eleProb = self.elementProbability(element,category)
		catProb = self.getCatCount(category)/self.totalCount()
		return float(eleProb*catProb)

	'''def categoryGivenElement(self,category,element):
		#P(category|element) = P(element|category) * P(category)
		total = 0
		probEle = 1 #ignored term
		for c in self.categories():
			total += self.getCatCount(c)
		catProb = self.getCatCount(category)/total
		return self.elementGivenCategory(element,category) * catProb / probEle'''

	def classify(self,element):
		findP = {}
		for c in self.categories():
			findP[c] = self.Final(element,c)
		'''maximum = 0.0
		category = None
		category = None
		for temp in findP:
			if findP[temp] > maximum:
				maximum = findP[temp]
				category = temp
		return (category,maximum)'''
		return findP
