#!/usr/bin/python
import io
import os
from numpy.core.fromnumeric import shape
from pandas import *
import numpy as np

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()
    
    values = []
    read_points = True
    instructions = []
    for line in lines:
        line = line.rstrip()
        if not line:
            read_points = False
            continue
        if read_points:
            values.append([int(c) for c in line.split(',')])
        else:
            fold = line.split(' ')[-1].split('=')
            instructions.append({fold[0]:int(fold[1])})
    print("read count:", len(values))
    return values, instructions

def doXFold(field, xs):
    s = np.shape(field)
    newField = np.zeros((xs, s[1]))
    for x in range(0, len(field)):
        for y in range(0, len(field[x])):
            if field[x][y] == 0:
                continue
            if x < xs:
                newField[x][y] = 1
                continue
            newX = 2*xs-x
            if newX < 0:
                continue
            newField[newX][y] = 1
    return newField

def doYFold(field, ys):
    s = np.shape(field)
    newField = np.zeros((s[0], ys))
    for x in range(0, len(field)):
        for y in range(0, len(field[x])):
            if field[x][y] == 0:
                continue
            if y < ys:
                newField[x][y] = 1
                continue
            newY = 2*ys-y
            if newY < 0:
                continue
            newField[x][newY] = 1
    return newField

def doInstructions(field, instructions):
    #print(DataFrame(field).transpose())
    for inst in instructions:
        #print("inst", inst)
        for k in inst:
            if k == "x":
                field = doXFold(field, inst[k])
            else:
                field = doYFold(field, inst[k])
        #break
    print(DataFrame(field).transpose())
    return field

def fillField(points):
    maxX = 0
    maxY = 0
    for pt in points:
        if maxX < pt[0]:
            maxX = pt[0]
        if maxY < pt[1]:
            maxY = pt[1]
    field = np.zeros([maxX+1, maxY+1])
    for pt in points:
        field[pt[0]][pt[1]] = 1
    return field

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

values, instructions = readValues(file_path)
#print(values)
#print(instructions)

field = fillField(values)
#print(DataFrame(field).transpose())
field = doInstructions(field, instructions)
print("res", int(np.sum(field)))
