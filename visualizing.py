import csv
def readData(filename):
    f = open(filename, "r")
    # Semester, 3 orig, 3 cleaned, 3 categories
    data = list(csv.reader(f))
    return data

data = readData("flavors.csv")

#

def getFlavorCounts(data, flavor):
    counts = []
    start = data[0].index("#1 Category")
    for i in range(1, len(data)):
        categories = data[i][start:start+3]
        count = categories.count(flavor)
        counts.append(count)
    return counts

print("Chocolate:", getFlavorCounts(data, "chocolate "))

#

def getIceCreamCounts(data):
    d = { }
    start = data[0].index("#1 cleaned")
    for i in range(1, len(data)):
        flavors = data[i][start:start+3]
        for flavor in flavors:
            if flavor not in d:
                d[flavor] = 0
            d[flavor] = d[flavor] + 1
    return d

counts = getIceCreamCounts(data)
for flavor in counts:
    print(flavor, counts[flavor])

###

import matplotlib.pyplot as plt

labels = [ "A", "B", "C", "D", "E" ]
yValues = [ 10, 40, 36, 46, 21 ]
colors = [ "red", "yellow", "green",
           "blue", "purple" ]
plt.bar(labels, yValues, color="red")
plt.xlabel("Products", loc="left")
plt.show()

###

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

x1 = []
x2 = []
for i in range(5):
    x1.append(i - width/2)
    x2.append(i + width/2)

plt.bar(x1, men_means, width, label='Men')
plt.bar(x2, women_means, width, label='Women')

plt.show()

###

import matplotlib.pyplot as plt

def combineUncommon(counts, cutoff):
    newCounts = { "other" : 0 }
    for flavor in counts:
        if counts[flavor] < cutoff:
            newCounts["other"] += counts[flavor]
        else:
            newCounts[flavor] = counts[flavor]
    return newCounts

counts = combineUncommon(getIceCreamCounts(data), 4)

flavors = []
flavorCounts = []
for flavor in counts:
    flavors.append(flavor)
    flavorCounts.append(counts[flavor])

plt.pie(flavorCounts, labels=flavors)

plt.show()