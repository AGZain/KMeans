import csv
import math
import numpy
x = []
y = []
with open('data/k-means/exercise-1.csv', 'rb') as csvfile:
	read = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in read:
		x.append(row[0])
		y.append(row[1])
x.pop(0)
y.pop(0)
print(x)
print(y)		
