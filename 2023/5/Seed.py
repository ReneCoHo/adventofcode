#!/usr/bin/python
import os

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

with open(file_path) as f:
    input = f.read()

maps, seeds = readInput(input)

lowest = min([product(maps, s) for s in seeds])

print("1:", lowest)


#print("2 sum:", np.array(cards).sum())