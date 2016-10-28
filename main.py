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
#arr = []
#for item in test_data:
#	arr.append(clf.test(item['abstract'],item['category']))
clf.test("The Swedish Act on Municipal Energy Planning was written in 1977 in a time of energy crisis and requires each municipality to have a plan for rational supply and distribution of energy. With regards to the on-going climate change however, there is a need for energy planning to emphasise on shifting towards an efficient energy system with high share of renewables, and low impacts on the climate and the environment.The legislation is therefore argued to be outdated and is currently under review. This study shows that most municipalities are working with the energy issue, as 71% have adopted a policy document with focus on energy and climate. However, 41% has not adopted an energy plan as referred to in the Act on municipal energy planning.The results show that the energy strategies have a wider focus than what is stated in the legislation, which strengthens the view that the legislation can be regarded as outdated. Energy Strategies however still have an important function at the municipal level, as they can help to integrate energy aspects into spatial planning, as well as function as support for the daily energy and climate work in the choice of strategies and measures.The study further shows that the use of Strategic Environmental Assessment has potential to increase the consideration of environmental quality objectives, especially those that might be impacted from the energy plans, but the use of it has been fairly limited and only conducted in 6% of the energy plans. It is therefore recommended that the Act on Municipal Energy Planning is revised to instead include requirements for municipal energy and climate strategies, and that they are made subject to Strategic Environmental Assessment, thus promoting a transition to a sustainable energy system, where environmental objectives are taken into account and possible conflicts can be addressed early in the planning process.",'Energy and Environment')
#Accuracy
#print float(sum(arr))/len(arr)
		 

	
