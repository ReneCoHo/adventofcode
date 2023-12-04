#!/usr/bin/python
import os
from collections import defaultdict

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")
figurs=set('1234567890')

def readInput(lines):
    mat=[] 
    for line in lines:
        mat.append([x for x in line])
    return mat

def checkMat(charMat):
    sum = 0
    star_adj = defaultdict(list)
    for r, line in enumerate(charMat):
        c = 0
        while  c < len(line):
            if not line[c].isdigit():
                c += 1
                continue

            figStart = c
            figEnd = c
            valid = False

            starPosition=None

            #move over figure and search for symbol
            while c < len(line) and line[c].isdigit():
                for rt, ct in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]:
                    if ct+c < len(line) and ct+c >= 0 and rt+r >= 0 and rt+r < len(line):
                        test=charMat[rt+r][ct+c]
                        if not(test=="." or test.isdigit()):
                            valid = True
                            if test == "*":
                                starPosition = (rt+r, ct+c)

                c += 1
                figEnd = c

            if valid:
                number = int(''.join(line[figStart:figEnd]))
                sum += number
                if starPosition:
                    star_adj[starPosition].append(number)

    return sum, star_adj

with open(file_path) as f:
    lines = f.read().splitlines()

charMat = readInput(lines)
sum, star_adj = checkMat(charMat)

print("1 sum:", sum)

ratio=0
for pos, numbers in star_adj.items():
    if len(numbers) == 2:
        ratio += numbers[0]*numbers[1]
print("2 sum:", ratio)