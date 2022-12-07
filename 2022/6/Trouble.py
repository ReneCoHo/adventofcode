#!/usr/bin/python
import os
import time

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

# create a new set for every subset
def find_start(data, header_len, start=0):
    for i in range(start, len(data) - header_len):
        if len(set(data[i:i + header_len])) == header_len:
            return i + header_len

# get the start time
st = time.time()

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    input = f.read()

sop = find_start(input, 4)
som = find_start(input, 14, sop)

print(sop)
print(som)
#print(findBegin(input, 4))
#print(findBegin(input, 14))

# get the execution time
elapsed_time = time.time() - st
print('Execution time:', elapsed_time, 'seconds')