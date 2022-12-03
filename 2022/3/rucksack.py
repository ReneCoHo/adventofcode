#!/usr/bin/python
import os

def calcPriority(lines):
    priority = 0
    for line in lines:
        line = line.rstrip()
        h = int(len(line)/2)
        test = set()
        for c in line[:h]:
            test.add(c)

        for c in line[h:]:

            if c in test:
                if c.islower():
                    priority += 1 + ord(c)-ord('a')
                else:
                    priority += 27 + ord(c)-ord('A')
                break
    return priority

def groupValue(line):
    groupValue = 0

    for i in range(0, len(lines), 3):
        line0 = line[i].rstrip()

        test = {}
        for c in line0:
            test[c] = 1
        
        line1 = line[i+1].rstrip()
        for c in line1:
            if c in test:
                test[c] = 2
            
        line2 = line[i+2].rstrip()
        for c in line2:
            if c in test:
                if test[c] == 2:
                    test[c] = 3
                    break

        for c, n in test.items():
            if n == 3:
                if c.islower():
                    groupValue += 1 + ord(c)-ord('a')
                else:
                    groupValue += 27 + ord(c)-ord('A')
                break

    return groupValue

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    lines = f.readlines()

#print(calcPriority(lines))
print(groupValue(lines))