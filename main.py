import csv
import math
import matplotlib.pyplot as plt
import numpy as np

def assignCluster(clusters, vals):
	lowest = (0,0)					#location, value
	new = True
	for i in range(0,len(clusters)):
		dist = math.sqrt(math.pow(float(vals[0])-float(clusters[i][0]),2.) + math.pow(float(vals[1])-float(clusters[i][1]),2.))
		print(dist)
		if dist < lowest[1] or new == True:
			lowest = (i+1, dist)
			new = False
	return lowest[0]

x = []
y = []
k = []
numOfC = 4


with open('data/k-means/exercise-2.csv', 'rb') as csvfile:
	read = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in read:
		x.append(row[0])
		y.append(row[1])

x.pop(0)
y.pop(0)
grps = [0]*numOfC
col = np.chararray(len(x))

for i in range(0,len(x)):
	x[i] = float(x[i])
	y[i] = float(y[i])

# for i in range(0,numOfC):				#sets initial cluster centroids
# 	k.append((x[i],y[i]))
# 	grps[i] += 1
# 	if i == 0:
# 		col[i] = 'r'
# 	elif i == 1:
# 		col[i] = 'b'
# 	elif i == 2:
# 		col[i] = 'k'
# 	elif i == 3:
# 		col[i] = 'm'
# 	elif i == 4:
# 		col[i] = 'y'
# k.append((4.,52.5))
# k.append((83.,21.))
# #k.append((111.,125.))
# k.append((36.,152.))
started = False
k1 = [0.,0.]
for i in range(0,len(x)):
	if started == False:
		k1[0] = x[i]
		k1[1] = y[i]
		started = True
	if x[i] >= k1[0] and y[i] >= k1[1]:
		k1[0] = x[i]
		k1[1] = y[i]
		print("FOUND: " + str(k1[0]) + "    " + str(k1[1]))
k.append((k1[0],k1[1]))
print("FOUND: " + str(k1[0]) + "    " + str(k1[1]))
k.append((0,0))
k.append((0,0))
k.append((0,0))
#PROBLEM IS HERE
for i in range(1,numOfC):
	dist = [None]*i
	lowestDist = 0
	for j in range(0,len(x)):
		dist[i-1] = math.sqrt(math.pow(float(x[j])-float(k[i-1][0]),2.) + math.pow(float(y[j])-float(k[i-1][1]),2.))
	if dist[i-1] > lowestDist:
		k[i] = (x[j],y[j])

for i in range(0,len(x)):
	group = assignCluster(k,(x[i],y[i]))
	print(group)
	grps[group-1] += 1
	k[group-1] = ((float(k[group-1][0])*grps[group-1] + float(x[i]))/(float(grps[group-1])+1),(float(k[group-1][1])*grps[group-1] + float(y[i]))/(float(grps[group-1])+1))
	#k[group-1] = ((float(k[group-1][0]) + float(x[i]))/2.,(float(k[group-1][1])*n + float(y[i]))/(n+1))
	print((x[i],y[i]))

	print(k[group-1])
	if group == 1:
		col[i] = 'r'
	elif group == 2:
		col[i] = 'b'
	elif group == 3:
		col[i] = 'k'
	elif group == 4:
		col[i] = 'm'
	elif group == 5:
		col[i] = 'y'

for z in range(0,1000):
	for i in range(0,len(x)):
		dist = [None]*numOfC
		new = True
		lowest = 0
		group = -1
		for j in range(0,numOfC):
			dist[j] = math.sqrt(math.pow(float(x[i])-float(k[j][0]),2.) + math.pow(float(y[i])-float(k[j][1]),2.))
			if new == True or lowest > dist[j]:
				lowest = dist[j]
				group = j
				new = False

		group += 1
		grps[group-1] += 1
		k[group-1] = ((float(k[group-1][0])*grps[group-1] + float(x[i]))/(float(grps[group-1])+1),(float(k[group-1][1])*grps[group-1] + float(y[i]))/(float(grps[group-1]+1)))
		if group == 1:
			col[i] = 'r'
		elif group == 2:
			col[i] = 'b'
		elif group == 3:
			col[i] = 'k'
		elif group == 4:
			col[i] = 'm'
		elif group == 5:
			col[i] = 'y'

plt.scatter(x,y,c=col,marker='o')
plt.show()
