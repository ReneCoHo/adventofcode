#!/usr/bin/python
import os

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")
#file_path = os.path.join(path, "input_small.txt")

def extrapol(values):
    if all(v == 0 for v in values):
        return 0
    
    diff = []
    for i in range(1, len(values)):
        diff.append(values[i] - values[i-1])
    return diff[-1] + extrapol(diff)

with open(file_path) as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:   
    int_list = [int(i) for i in line.split(" ")]
    sum += int_list[-1] + extrapol(int_list)


print("1 sum:", sum)