#!/usr/bin/python
import os

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    lines = f.readlines()

moves  = []
line_stacks = []
move_lines=False

for line in lines:

    if line == '\n':
        move_lines = True
        continue
    if move_lines:
        line = line.split()
        moves.append((int(line[1]), int(line[3]), int(line[5])))
    elif '[' in line:
        letters=[]       
        for i, column in enumerate(line):
            if i % 4 == 1:
                letters.append(column.lstrip())
        line_stacks.append(letters)

stacks = [None, [], [], [], [], [], [], [], [],[]]
for j in range(len(line_stacks)-1, -1, -1):
    for i, letter in enumerate(line_stacks[j]):
        if letter == '':
            continue
        stacks[i+1].append(letter)

for n, i, j in moves:
	chunk = stacks[i][-n:]
	stacks[i] = stacks[i][:-n]
	stacks[j] = stacks[j] + chunk[::-1]

top = ''.join(s[0] for s in stacks[:][-1])

print(top)
#FBVRFHNSB
#BCRHWLBQMQP
# BSDMQFLSP