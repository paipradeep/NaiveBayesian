import splitt
from BClassify import BayesianClassifier
obj = BayesianClassifier(splitt.getWords)
s = raw_input()
print(obj.classify(s))
