# coding=utf-8
from classifier import Classifier 
import csv
import random
from pandas import DataFrame

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
print len(test_data)
clf = Classifier(categories)

#Training
for item in train_data:
	clf.train(item['abstract'],item['category'])

#Testing
arr = []
for item in test_data:
	arr.append(clf.test(item['abstract'],item['category']))

#Confusion Matrix
name_to_num = {}
for i,category in enumerate(categories):
	name_to_num[category] = i

n = len(categories)
conf_mat = [[0 for col in range(n)] for row in range(n)]
for item in test_data:
	conf_mat[name_to_num[item['category']]][name_to_num[clf.predict(item['abstract'])]] += 1 

print DataFrame(conf_mat)

#Accuracy
print float(sum(arr))/len(arr)
		 
for key, value in name_to_num.items():
    print value,key
	