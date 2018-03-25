import csv
import math
import matplotlib.pyplot as plt

def assignCluster(clusters, vals):
	lowest = (0,0)					#location, value
	new = True
	for i in range(0,len(clusters)):
		dist = math.sqrt(math.pow(float(vals[0])-float(clusters[i][0]),2) + math.pow(float(vals[1])-float(clusters[i][1]),2))
		if dist < lowest[1] or new == True:
			lowest = (i+1, dist)
			new = False
	return lowest[0]

x = []
y = []
cluster = []
k = []
numOfC = 5
with open('data/k-means/exercise-1.csv', 'rb') as csvfile:
	read = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in read:
		x.append(row[0])
		y.append(row[1])

x.pop(0)
y.pop(0)

for i in range(0,numOfC):				#sets initial cluster centroids
	k.append((x[i],y[i]))

for i in range(numOfC,len(x)):
	print(assignCluster(k,(x[i],y[i])))

plt.plot(5,5,'bo')
plt.plot(6,6,'ro')
plt.show()
