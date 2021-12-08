#!/usr/bin/python
import io
import os

def readSweeps(file_path):
    file_in = open(file_path, 'r')
    sweeps = []
    for line in file_in:
        sweeps.append(int(line))

    file_in.close()
    return sweeps

def countSimple(sweeps):
    if not sweeps:
        return 0

    count = 0
    last = sweeps[0]

    for sweep in sweeps:
        curr = sweep
        if last < curr:
            count += 1
        last = curr
    return count

def countWindow(sweeps):
    length = len(sweeps)
    if length < 3:
        return 0
    currSum = sweeps[0] + sweeps[1]
    lastSum = currSum + sweeps[2]
    count = 0
    i = 1
    while i < length - 1 :
        currSum += sweeps[i+1]
        if lastSum < currSum:
            count += 1
        print("i", i, ":", currSum)
        lastSum = currSum
        currSum -= sweeps[i-1]
        i += 1

    return count

path = os.path.dirname(__file__)

file_path = os.path.join(path, "input.txt")
sweeps = readSweeps(file_path)

count = countSimple(sweeps)
print("simple increase count:", count)

count = countWindow(sweeps)
print("window increase count:", count)
