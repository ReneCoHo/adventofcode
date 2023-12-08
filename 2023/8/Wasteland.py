#!/usr/bin/python
import os
import re
import itertools
from math import gcd

def steps(graph, instructions, start, ends):
    node = start
    step_n = 0
    for inst in itertools.cycle(instructions):
        if inst == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        step_n+=1
        if node in ends:
            break
    return step_n

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    input = f.read().split("\n\n")

instructions = input[0]
lines = input[1].splitlines()
starts=[]
ends=[]

graph = {}

for line in lines:
    knot, a, b = re.findall('\w+', line)
    graph[knot] = (a,b)

    if knot[-1] == "A":
        starts.append(knot)
    if a[-1] == "Z":
        ends.append(a)
    if b[-1] == "Z":
        ends.append(b)

n = steps(graph, instructions, "AAA", ["ZZZ"])
print("1:", n)

step_counts=[]
for start in starts:
    n = steps(graph, instructions, start, ends)
    step_counts.append(n)

lcm = 1
for i in step_counts:
    lcm = lcm*i//gcd(lcm, i)

print("2:", lcm)
