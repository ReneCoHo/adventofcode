#!/usr/bin/python
import io
import os
import numpy as np

def readValues(file_path):
    print("read file:", file_path)
    file_in = open(file_path, 'r')
    parts = file_in.readline().rstrip().split(",")
    values = [int(s) for s in parts if s]
    file_in.close()
    #print(values)
    print("read count:", len(values))
    return values

def dist(field, pos):
    gen = (abs(f - pos) for f in field)
    return np.sum(np.fromiter(gen, int))
    #s = 0
    #for f in field:
    #    s += abs(f - pos)
    #return s

def dist2(field, pos):
    gen = (abs(f - pos) for f in field)
    gen = ((d+1)*(d)/2 for d in gen)
    return np.sum(np.fromiter(gen, int))
    #s = 0
    #for f in field:
    #    d = abs(f - pos)
    #    s += (d+1)*(d)/2
    #return s

def searchMin(field, func):
    begin = min(field)
    end = max(field)
    minimum = begin
    minimumCost = func(field, field[minimum])

    for i in range(begin, end + 1):
        cost = func(field, i)
        if minimumCost > cost:
            minimumCost = cost
            minimum = i
        else:
            break
    return [minimum, minimumCost]

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

field = readValues(file_path)

median = np.median(field)
print("median:", median, "cost:", dist(field, median))
print("")

[p, c] = searchMin(field, dist)
print("pos:", p, "cost:", c)

[p, c] = searchMin(field, dist2)
print("pos2:", p, "cost:", c)

#p = np.mean(np.absolute(field - np.mean(field)))
#print("p", p)