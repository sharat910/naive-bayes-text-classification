# coding=utf-8
from classifier import Classifier 
import csv
import random

categories = []

data = []

with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile,fieldnames = ["abstract","category"])
	for row in reader:
		data.append({'abstract':row['abstract'],'category':row['category']})
		if row['category'] not in categories:
			categories.append(row['category'])

random.shuffle(data)

train_data = data[:200]
test_data = data[200:]

clf = Classifier(categories)

#Training
for item in train_data:
	clf.train(item['abstract'],item['category'])

#Testing
arr = []
for item in test_data:
	arr.append(clf.test(item['abstract'],item['category']))

#Accuracy
print float(sum(arr))/len(arr)
		 

	