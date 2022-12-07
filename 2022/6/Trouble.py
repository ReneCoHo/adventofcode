#!/usr/bin/python
import os

def findBegin(input, length):
    subCmp = {}
    subset = [ c for c in input[:length] ]

    for c in subset[:-1]:
        if c in subCmp:
            subCmp[c] += 1
        else :
            subCmp[c] = 1

    for i, c in enumerate(input[length-1:]):
        if c in subCmp:
            subCmp[c] += 1
        else :
            subCmp[c] = 1
        subset[length-1] = c
        if len(subCmp) == length:
            return i + length

        if subCmp[subset[0]] == 1:
            subCmp.pop(subset[0])
        else:
            subCmp[subset[0]] -= 1
        for i in range(0, length-1):
            subset[i] = subset[i+1]
    return None

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    input = f.read()

print(findBegin(input, 4))
print(findBegin(input, 14))