#!/usr/bin/env python3
import os
from copy import deepcopy

def readField(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    field = []
    for line in lines:
        field.append(list(line.rstrip()))
    return field

def doStep(field):
    out_field = deepcopy(field)
    rows = len(field)
    cols = len(field[0])
    change = False

    for y in range(rows):
        for x in range(cols):
            if field[y][x] == '>' and field[y][(x+1)%cols]=='.':
                out_field[y][x]='.'
                out_field[y][(x+1)%cols]='>'
                change = True
    field = deepcopy(out_field)
    for y in range(rows):
        for x in range(cols):
            if field[y][x] == 'v' and field[(y+1)%rows][x]=='.':
                out_field[y][x]='.'
                out_field[(y+1)%rows][x]='v'
                change = True

    return out_field, change


path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

field = readField(file_path)
#print(field)
#f = [''.join(l) for l in field]
#print(f)
change = True
s = 0
while change:
    field, change = doStep(field)
    #print([''.join(l) for l in field])
    s += 1

print("steps", s)