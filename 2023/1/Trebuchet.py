#!/usr/bin/python
import os
import numpy as np

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")
#file_path = os.path.join(path, "test2.txt")

digit_words = {
	'zero' : 0,
	'one'  : 1,
	'two'  : 2,
	'three': 3,
	'four' : 4,
	'five' : 5,
	'six'  : 6,
	'seven': 7,
	'eight': 8,
	'nine' : 9,
}

def readDigits(lines):
    digits = []
    for line in lines:

        for c in line:
            if c.isdigit():
                c0 = int(c)
                break
        for c in reversed(line):            
            if c.isdigit():
                c1 = int(c)
                break
            
        digits.append(10*c0 + c1)

    return np.array(digits)

def readNamedDigits(lines):
    digits = []
    line_num = 0
    for line in lines:
        #print("line:", line_num)
        line_num += 1
        c0 = int(0)
        c1 = int(0)

        for  i in range(len(line)):
            if line[i].isdigit():
                c0 = int(line[i])
                break
            else :
                r = next(filter(line[i:].startswith, digit_words), None)
                if r:
                    #print("r:", r)
                    c0 = int(digit_words.get(r, 0))
                    break
        for  i in range(len(line)-1, -1, -1):          
            if line[i].isdigit() :
                c1 = int(line[i])
                break
            else :
                r = next(filter(line[i:].startswith, digit_words), None)
                if r:
                    #print("r:", r)
                    c1 = int(digit_words.get(r, 0))
                    break
            
        digits.append(10*c0 + c1)

    return np.array(digits)

with open(file_path) as f:
    lines = f.readlines()

values = readDigits(lines)
print("1 sum:", values.sum())

values = readNamedDigits(lines)
#print(values)
print("2 sum:", values.sum())
