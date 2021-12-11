#!/usr/bin/python
import io
import os
import numpy as np
from numpy.core.fromnumeric import size

def readValues(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    ny = len(lines)
    nx = len(list(lines[0].rstrip()))

    field = np.zeros((ny, nx), dtype=int)
    for i in range(0, ny):
        chars = list(lines[i].rstrip())
        field[i,:] = [int(c) for c in chars if c]

    print("read count:", np.shape(field))
    return field

def getLowRisks(field):
    s = np.shape(field)
    low_risks = []
    for y in range(0, s[0]):
        for x in range(0, s[1]):
            if x > 0 and field[y][x] >= field[y][x-1] :
                continue
            if y > 0 and field[y][x] >= field[y-1][x] :
                continue
            if y+1 < s[0] and field[y][x] >= field[y+1][x] :
                continue
            if x+1 < s[1] and field[y][x] >= field[y][x+1] :
                continue
            low_risks.append((y, x))
    return low_risks

def countRisks(risks, field):
    sum = 0
    for r in risks:
        sum += field[r[0]][r[1]] + 1
    return sum

def calculateBasins(risks, field):
    basin_sizes = []
    for r in risks:
        basin_sizes.append(countSize(r, field))
    return basin_sizes

def countSize(start, field):
    s = np.shape(field)
    count = 1
    stack = []
    stack.append(start)
    used = {start}

    while len(stack) > 0:
        pos = stack.pop()
        p1 = (pos[0]-1, pos[1])
        if pos[0] > 0 and not (p1 in used) and field[p1[0]][p1[1]] != 9 :
            count += 1
            stack.append(p1)
            used.add(p1)
        p1 = (pos[0], pos[1]-1)
        if pos[1] > 0 and not (p1 in used) and field[p1[0]][p1[1]] != 9 :
            count += 1
            stack.append(p1)
            used.add(p1)
        p1 = (pos[0]+1, pos[1])
        if pos[0]+1 < s[0] and not (p1 in used) and field[p1[0]][p1[1]] != 9 :
            count += 1
            stack.append(p1)
            used.add(p1)
        p1 = (pos[0], pos[1]+1)
        if pos[1]+1 < s[1] and not (p1 in used) and field[p1[0]][p1[1]] != 9 :
            count += 1
            stack.append(p1)
            used.add(p1)

    return count

def calculateProduct(risks, field):
    sizes = calculateBasins(risks, field)
    sizes.sort(reverse=True)
    #print("sizes:", sizes)
    return sizes[0]*sizes[1]*sizes[2]

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")
field = readValues(file_path)
#print("field:", field)
risks = getLowRisks(field)

print(risks)
print("sum:", countRisks(risks, field))
print("product:", calculateProduct(risks, field))