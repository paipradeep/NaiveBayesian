import splitt
import csv
from BClassify import BayesianClassifier
obj = BayesianClassifier(splitt.getWords)
f = open("dataset.csv",'rb')
r = csv.reader(f)
headerline = f.next()
for row in r:
    #print row[2] + " " + row[6]
    if(int(row[2])>0):
        obj.train(row[6],"yes")
    else:
        obj.train(row[6],"no")
#print obj.fCount
#print obj.catCount
obj.saveDict()
# try taking input from a csv file
