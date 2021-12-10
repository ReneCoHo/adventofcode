#!/usr/bin/python
import io
import os
import numpy as np

def readValues(file_path):
    file_in = open(file_path, 'r')
    line = file_in.readline()
    line_strings = line.rstrip().split(',')
    values = [int(s) for s in line_strings if s]
    file_in.close()
    print("read count:", len(values))
    return values

def cost(value, pos):
    sum = 0
    for v in values:
        t =  abs(v - pos)
        print(t)
        sum += abs(v - pos)
    return sum

def simple(values):
    pos = np.median(values)
    c = cost(values, pos)
    print("pos:", pos, "cost:", c)

def expensive(values):

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")
values = readValues(file_path)
#simple(values)
expensive(values)

