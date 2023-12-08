#!/usr/bin/python
import os
import re
import itertools

def steps(graph, instructions):

    node = "AAA"
    step_n = 0
    for inst in itertools.cycle(instructions):
        if inst == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        step_n+=1
        if node == "ZZZ":
            break
    return step_n

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    input = f.read().split("\n\n")

instructions = input[0]
lines = input[1].splitlines()

graph = {}

for line in lines:
    knot, a, b = re.findall('\w+', line)
    graph[knot] = (a,b)

n = steps(graph, instructions)
print("1:", n)
