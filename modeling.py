### LOAD DATA ###

# Header:
# Semester,
# #1 Orig,     #2 Orig,     #3 Orig,
# #1 Cleaned,  #2 Cleaned,  #3 Cleaned,
# #1 Category, #2 Category, #3 Category

import csv
f = open("all-icecream.csv", "r")
orig = list(csv.reader(f))
data = []
test = []
for line in orig:
    if line[0] != "Semester": # skip header
        # only include coded classes
        categories = line[7:10]
        if line[0] == "S21":
            test.append(categories)
        else:
            data.append(categories)
f.close()

### HELPER FUNCTIONS ###

def getAllFlavors(data):
    allFlavors = [ ]
    for line in data:
        if line[2] not in allFlavors:
            allFlavors.append(line[2])
    return allFlavors

def bestGuess(flavorProbs):
    bestFlavor = None
    bestProb = -1
    for flavor in flavorProbs:
        if flavorProbs[flavor] > bestProb:
            bestProb = flavorProbs[flavor]
            bestFlavor = flavor
    return bestFlavor


### NAIVE BAYES TRAINING ###

# Probability that a flavor is chosen
def getClassProb(data, flavor):
    count = 0
    for line in data:
        if line[2] == flavor:
            count += 1
    return count / len(data)

# Probability that 1st/2nd favorite is X given that 3rd favorite is C
def getCondProb(data, priorFlavor, thirdFlavor, priorIndex):
    count = 0
    total = 0
    for line in data:
        if line[2] == thirdFlavor:
            total += 1 # only count entries with third flavor
            if line[priorIndex] == priorFlavor:
                count += 1
    return count / total

# Format probabilities nicely
def prob(num):
    return str(round(num*100, 2)) + "%"

# Given 1st and 2nd favorites, what is the most likely 3rd?
def predict(data, first, second, showWork=False):
    flavorProbs = { }
    allFlavors = getAllFlavors(data) # possible flavors
    for flavor in allFlavors:
        flavorProb = getClassProb(data, flavor)
        firstProb = getCondProb(data, first, flavor, 0)
        secondProb = getCondProb(data, second, flavor, 1)
        overallProb = firstProb * secondProb * flavorProb
        if showWork:
            print(flavor, prob(overallProb), "-", prob(firstProb), prob(secondProb), prob(flavorProb))
        flavorProbs[flavor] = overallProb
    return bestGuess(flavorProbs) # find best value

print("PREDICTION:", predict(data, "chocolate", "vanilla", showWork=True))

### TEST ###

# Test each element in the test set based on the model
def runDataset(modelData, testData):
    guessedRight = 0
    for line in testData:
        predictFav = predict(modelData, line[0], line[1])
        actualFav = line[2]
        if predictFav == actualFav:
            guessedRight += 1
    return guessedRight/len(testData)

print("TESTING RESULT:", runDataset(data, test))