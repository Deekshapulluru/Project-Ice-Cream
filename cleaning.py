f = open("icecream.csv", "r")
text = f.read()
f.close()

###

f2 = open("something.txt", "w")
f2.write("Hi there!")
f2.close()

###

s = "A\\B"
print(s)

###

import csv

f = open("icecream.csv", "r")
reader = csv.reader(f)

data = [ ]
for row in reader:
    data.append(row)

print(data)

f.close()

###

import json

f = open("icecream.json", "r")
j = json.load(f)

print(j)

f.close()

###

f = open("chat.txt", "r")
text = f.read()
f.close()

people = [ ]
for line in text.split("\n"):
    start = line.find("From") + \
            len("From")
    line = line[start:]
    end = line.find(" : ")
    line = line[:end]
    if "(Direct Message)" in line:
        end = line.find("to")
        line = line[:end]
    line = line.strip()
    people.append(line)
print(people)

###

# Assume data is a 2D list parsed from the file above
header = data[0]
header.pop(0) # remove the ID
header.append("# chocolate")
for row in range(1, len(data)):
    data[row].pop(0) # remove the ID
    chocCount = 0 # count number of chocolate
    for col in range(len(data[row])):
        # Make all flavors lowercase
        data[row][col] = data[row][col].lower()
        if "chocolate" in data[row][col]:
            chocCount += 1
    # track chocolate count
    data[row].append(chocCount)
print(data)
