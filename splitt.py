import re

def getWords(item):
	sp = re.compile('\\W*')
	l = sp.split(item)
	words = []
	for temp in l:
		if len(temp)>2:
			words.append(temp.lower())
	uniqueWords = {}
	for w in words:
		uniqueWords[w] = 1
	return uniqueWords
