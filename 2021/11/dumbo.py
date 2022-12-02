#!/usr/bin/python
import io
import os

from pandas import *

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()
    
    values = []
    for line in lines:
        values.append([int(c) for c in line.rstrip()])
    print("read count:", len(values))
    return values

def increaseAll(field, inc):
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j] += inc

def increase(field, inc, has_flashed, flash_octo, i, j):
    if i < 0 or j < 0 or i >= len(field) or j >= len(field):
        return
    if (i,j) in has_flashed:
        return
    field[i][j] += 1
    if field[i][j] > 9:
        flash_octo.append((i, j))

def step(field):
    increaseAll(field, 1)
    has_flashed = set()
    flash_octo = []
    
    # fill start
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] > 9:
                flash_octo.append((i, j))

    it = 0
    while flash_octo:
    #while flash_octo and it < 10:
        it += 1
        (i, j) = flash_octo.pop()
        if (i, j) in has_flashed:
            continue

        has_flashed.add((i, j))
        field[i][j]=0
        increase(field, 1, has_flashed, flash_octo, i-1, j-1)
        increase(field, 1, has_flashed, flash_octo, i-1, j)
        increase(field, 1, has_flashed, flash_octo, i-1, j+1)
        increase(field, 1, has_flashed, flash_octo, i, j-1)
        increase(field, 1, has_flashed, flash_octo, i, j+1)
        increase(field, 1, has_flashed, flash_octo, i+1, j-1)
        increase(field, 1, has_flashed, flash_octo, i+1, j)
        increase(field, 1, has_flashed, flash_octo, i+1, j+1)

    return len(has_flashed)

def flashes(field, step_count):
    flash_count = 0
    for i in range(0, step_count):
        f = step(field)
        if f == 100:
            print("all flash", i+1, "|", f)
        #print("step i", i+1)
        #print(DataFrame(field))
        flash_count += f
    return flash_count

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "test2.txt")
file_path = os.path.join(path, "input.txt")

values = readValues(file_path)

step_count = 500
print("flashes", flashes(values, step_count))
