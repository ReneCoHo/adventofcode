#!/usr/bin/python
import os

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

file_in = open(file_path, 'r')
max_calories=[int(0),int(0),int(0)]
curr_calories=int(0)
max_calories

for line in file_in:
    line = line.rstrip()
    if line:
        curr_calories += int(line)
    else:
        for i in range(0, 3):
            if curr_calories > max_calories[i]:
                max_calories[i] = curr_calories
                break
        curr_calories = 0

print("sum max:", max_calories[0] + max_calories[1] + max_calories[2])