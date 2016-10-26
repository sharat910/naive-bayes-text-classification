import matplotlib.pyplot as plt
from train import *


low=0
high=10
flag=1
train_line_x=[1]
test_line_x=[1]
y=[0]
while flag==1:
	if high==700
		flag=0
	for x in range(low,high):
		train(dict_data.keys()[x], dict_data[dict_data.keys()[x]])

	train_correct=0
	train_incorrect=0	
	for item in dict_data:
		prediction=test(item)
		if	prediction==dict_data[item]:
			train_correct=train_correct+1
		else:
			train_incorrect=train_incorrect+1

	test_correct=0
	test_incorrect=0
	for item in dict_test:
		prediction=test(item)
		if	prediction==dict_test[item]:
			test_correct=test_correct+1
		else:
			test_incorrect=test_incorrect+1
	
	train_error=train_incorrect/(train_incorrect+train_correct)
	test_error=test_incorrect/(test_incorrect+test_correct)
	train_line_x.append(train_error)
	test_line_x.append(test_error)
	
	y.append(high)
	low=high
	high=high+10

plt.plot(train_error,y,'r')
plt.plot(test_error,y,'b')
plt.show()	

