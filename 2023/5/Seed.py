#!/usr/bin/python
import os
import numpy as np
from collections import deque
from operator import itemgetter

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")
#file_path = os.path.join(path, "test.txt")

def filter_ints(txt):
    return True if txt.isdigit() else False

def readInput(input):
    sections = input.split("\n\n")
    t = sections[0].split(" ")
    seeds = list(filter(filter_ints, t))
    seeds = [int(x) for x in seeds]
    maps = []
    for s in sections[1:]:
        lines = s.split("\n")
        m = []
        for line in lines[1:]:
            t = line.split(" ")
            t = list(filter(filter_ints, t))
            m.append([int(x) for x in t])
        maps.append(m)

    return maps, seeds

def product(maps, seed):
    for m in maps:
       for mapLine in m:
           if (seed >=  mapLine[1]) and (seed < mapLine[1] + mapLine[2]):
               seed = seed + mapLine[0] - mapLine[1]
               break
           
    return seed

def overlap(a, b, c, d):
	return not (a > d or b < c)

def minRange(maps, seeds):
    # start ranges
    ss = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    current = [(a, a + b - 1) for a, b in ss]
    current = deque(current)

    for step in maps:
        new = deque()

        while current:
            a, b = current.popleft()

            for dst, src, sz in step:
                c = src
                d = src + sz - 1
                delta = dst - src

                if not overlap(a, b, c, d):
                    continue

                # C---a---b---D completely inside
                #     xxxxx
                if c <= a <= d and c <= b <= d:
                    new.append((a + delta, b + delta))
                    break

                # a---C---b---D escapes left
                #     xxxxx
                if c <= b <= d:
                    # C---b (overlap)
                    new.append((c + delta, b + delta))
                    # a---C (no overlap)
                    current.append((a, c - 1))
                    break

                # C---a---D---b escapes right
                #     xxxxx
                if c <= a <= d:
                    # C---D (overlap)
                    new.append((a + delta, d + delta))
                    # D---b (no overlap)
                    current.append((d + 1, b))
                    break

                # a---C---D---b escapes both sides
                #     xxxxx
                if a < c and b > d:
                    # C---D (overlap)
                    new.append((c + delta, d + delta))
                    # a---C (no overlap)
                    # D---b (no overlap)
                    current.append((d + 1, b))
                    current.append((a, c - 1))
                    break
            else:
                # no overlap with any segment
                new.append((a, b))

        current = new
    x = map(itemgetter(0), current)    
    return min(x)

with open(file_path) as f:
    input = f.read()

maps, seeds = readInput(input)

lowest1 = min([product(maps, s) for s in seeds])
print("1:", lowest1)

lowest2 = minRange(maps, seeds)
print("2:", lowest2)
