#!/usr/bin/python
import os
import numpy as np

def readValues(file_path):
    file_in = open(file_path, 'r')
    values = []
    maxVal = 0
    for line in file_in:
        line_parts = line.rstrip().split(' ')
        if len(line_parts) != 2 :
            # skip
            continue
        if line_parts[0] == 'on':
            inst = [True]
        else:
            inst = [False]

        coords = line_parts[1].split(',')
        for coord in coords:
            p = coord[2:].split("..")
            maxVal = max(maxVal, int(p[0]))
            maxVal = max(maxVal, int(p[1]))
            inst += [(int(p[0]), int(p[1])) ]
        values.append(inst)

    file_in.close()
    print("read count:", len(values))
    return values, maxVal

def areOverlap(a : tuple, b: tuple)->bool:
    return a[0][1] >= b[0][0] and b[0][1]>=a[0][0] and \
        a[1][1] >= b[1][0] and b[1][1]>=a[1][0] and \
        a[2][1] >= b[2][0] and b[2][1]>=a[2][0]


def doInstructions(volume, instructions):
    n2 = len(volume) // 2
    area = ((-n2, n2),(-n2, n2),(-n2, n2))
    for inst, x, y, z in instructions:
        if not areOverlap(area, (x,y,z)):
            continue
        for ix in range(x[0], x[1]+1):
            for iy in range(y[0], y[1]+1):
                for iz in range(z[0], z[1]+1):
                    if inst:
                        volume[n2+iz][n2+iy][n2+ix] = 1
                    else:
                        volume[n2+iz][n2+iy][n2+ix] = 0
    return volume

def countOnes(volume):
    count = 0
    n = len(volume)
    for z in range(n):
        for y in range(n):
            for x in range(n):
                if volume[z][y][x]:
                    count+=1
    return count

path = os.path.dirname(__file__)
file_path = os.path.join(path, "test3.txt")
file_path = os.path.join(path, "input.txt")
instructions, maxVal = readValues(file_path)
print(maxVal)

maxVal = 50
volume = np.zeros((2*maxVal+1,)*3)
volume = doInstructions(volume, instructions)
print(countOnes(volume))

