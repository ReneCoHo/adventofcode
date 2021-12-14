#!/usr/bin/python
import io
import os

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    start = lines[0].rstrip()
    instructions = []
    for i in range(2, len(lines)):
        parts = lines[i].rstrip().split(' ')
        instructions.append((parts[0], parts[2]))
    return start, instructions


path = os.path.dirname(__file__)
file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "test2.txt")
#file_path = os.path.join(path, "input.txt")

start, instructions = readValues(file_path)

print(start)
print(instructions)

for ins in instructions:
    for c in start:
        if ins[0] 