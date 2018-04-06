import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import time

def color(grp):                 #method to return the colour of the group
    if grp == 1:
        return 'r'
    elif grp == 2:
        return 'b'
    elif grp == 3:
        return 'k'
    elif grp == 4:
        return 'm'
    elif grp == 5:
        return 'y'

def assignCluster(clusters, vals):  #assign points to intial cluster
	lowest = (0,0)					#location, value
	new = True
	for i in range(0,len(clusters)):   #Loop through each cluster
		dist = math.sqrt(math.pow(float(vals[0])-float(clusters[i][0]),2.) + math.pow(float(vals[1])-float(clusters[i][1]),2.))
		if dist > lowest[1] or new == True:
			lowest = (i+1, dist)
			new = False
	return lowest[0]

def start():                            #Get data from files
    with open('data/k-means/exercise-2.csv', 'r') as csvfile:
    	read = csv.reader(csvfile,delimiter=',',quotechar='|')
    	for row in read:
    		x.append(row[0])             #Add x and y points
    		y.append(row[1])

    x.pop(0)                             #Remove the headings of the columns
    y.pop(0)

    for i in range(0,len(x)):
    	x[i] = float(x[i])
    	y[i] = float(y[i])

def initialClusters():
    for i in range(0,numOfC):				#sets initial cluster centroids
        k.append((x[i],y[i]))
        grps[i] += 1
        col[i] = color(i+1)
def assignAll():
    for i in range(0,len(x)):
        group = assignCluster(k,(x[i],y[i]))
        grps[group-1] += 1
        k[group-1] = ((float(k[group-1][0])*grps[group-1] + float(x[i]))/(float(grps[group-1])+1),(float(k[group-1][1])*grps[group-1] + float(y[i]))/(float(grps[group-1])+1))
        col[i] = color(group)

def confirm():                                  #reassigning clusters
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
            theCol = color(group)
            if theCol != col[i]:
                col[i] = theCol

start_time = time.time()
x = []
y = []
k = []
numOfC = 4
grps = [0]*numOfC
start()
col = np.chararray(len(x))
initialClusters()
assignAll()
confirm()
print("--- %s seconds ---" % (time.time() - start_time))
plt.scatter(x,y,c=col,marker='o')
plt.show()
