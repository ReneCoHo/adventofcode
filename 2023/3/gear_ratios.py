#!/usr/bin/python
import os

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
    for r, line in enumerate(charMat):
        c = 0
        while  c < len(line):
            if not line[c].isdigit():
                c += 1
                continue

            figStart = c
            figEnd = c
            valid = False

            #move over figure and search for symbol
            while c < len(line) and line[c].isdigit():
                if not valid:
                    for rt, ct in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]:
                        if ct+c < len(line) and ct+c >= 0 and rt+r >= 0 and rt+r < len(line):
                            test=charMat[rt+r][ct+c]
                            if not(test=="." or test.isdigit()):
                                valid = True
                                break
                c += 1
                figEnd = c

            if valid:
                number = int(''.join(line[figStart:figEnd]))
                sum += number
    return sum

with open(file_path) as f:
    lines = f.read().splitlines()

charMat = readInput(lines)
sum = checkMat(charMat)

print("1 sum:", sum)

#print("2 sum:", power)