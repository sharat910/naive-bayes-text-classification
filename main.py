# coding=utf-8
from classifier import Classifier 
import csv
import random

categories = ['Energy and Environment', 'Material Science', 'Signal Processing', 'Economics and Finance', 'Health and Nutrition', 'Software Design']

clf = Classifier(categories)

data = []
with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile,fieldnames = ["abstract","category"])
	for row in reader:
		data.append({'abstract':row['abstract'],'category':row['category']})

print len(data)
random.shuffle(data)

train_data = data[:200]
test_data = data[200:]

#Training
for item in train_data:
	clf.train(item['abstract'],item['category'])

#Testing
arr = []
for item in test_data:
	arr.append(clf.test(item['abstract'],item['category']))


print float(sum(arr))/len(arr)
		 

	