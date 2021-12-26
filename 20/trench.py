#!/usr/bin/python
import os
from pandas import *

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()
    translate = []
    for c in lines[0].rstrip():
        if c == '#':
            translate.append(1)
        else:
            translate.append(0)
    field = []
    for i in range(2, len(lines)):
        r = []
        for c in lines[i].rstrip():
            if c == '#':
                r.append(1)
            else:
                r.append(0)
        field.append(r)
    print("size", len(field), len(field[0]))
    return translate, field

def enhance(field, M):
    N = len(field)
    return [[0]*(N + 2*M) for _ in range(M)] + [[0]*M + row + [0]*M for row in field] +[[0]*(N + 2*M) for _ in range(M)]

def convert(translate, field):
    deltas = [(1, 1), (0, 1), (-1, 1), (1, 0), (0, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)]
    n = len(field)
    e_field = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            v = 0
            s = 0
            for dx, dy in deltas:
                x = i+dx
                y = j+dy
                if 0 <= x and x < n and 0 <= y and y < n:
                    v += field[y][x] << s
                s+=1

            #e_field[j][i] = v
            e_field[j][i] = translate[v]

    #print(DataFrame(e_field))
    return e_field

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

translate, field = readValues(file_path)

#print(translate)
#print(DataFrame(field))
run_count = 50
field = enhance(field, 2*run_count)
#print(DataFrame(field))
for _ in range(run_count):
    field = convert(translate, field)

#print(DataFrame(field))
count_lights_int = lambda b, I: sum(r[I:-I].count(1) for r in b[I:-I])
print("count:", count_lights_int(field, run_count))
