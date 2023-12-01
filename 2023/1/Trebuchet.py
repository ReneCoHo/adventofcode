#!/usr/bin/python
import os
import numpy as np

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")
#file_path = os.path.join(path, "test.txt")

def readDigits(lines):
    digits = []
    for line in lines:

        for c in line:
            if c.isdigit():
                c0 = c
                break
        for c in reversed(line):            
            if c.isdigit():
                c1 = c
                break
            
        digits.append(int(c0 + c1))

    return np.array(digits)

with open(file_path) as f:
    lines = f.readlines()

digits = readDigits(lines)
#print("digits:", digits)
print("sum:", digits.sum())
