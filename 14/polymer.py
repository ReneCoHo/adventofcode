#!/usr/bin/python
import os
import time

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    first_line = lines[0].rstrip()
    start = [char for char in first_line]
    instructions = {}

    for i in range(2, len(lines)):
        parts = lines[i].rstrip().split(' ')
        instructions[parts[0]] = parts[2]
    return start, instructions

def step( polymer, instructions):
    i = 1
    while i < len(polymer):
        curr = ''.join(polymer[i-1:i+1])
        if curr in instructions:
            polymer.insert(i, instructions[curr])
            i += 1
        i += 1
    return polymer

def steps( polymer, instructions, count):
    for i in range(0, count):
        step(polymer, instructions)
    return polymer

def segmentedStep(segments, instructions):
    new_segments = {}
    for (seg_k, seg_count) in segments.items():
        if seg_k in instructions:
            a = ''.join([instructions[seg_k], seg_k[1]])
            b = ''.join([seg_k[0], instructions[seg_k]])
            if a in new_segments:
                new_segments[a] += seg_count
            else :
                new_segments[a] = seg_count
            if b in new_segments:
                new_segments[b] += seg_count
            else:
                new_segments[b] = seg_count
    return new_segments

def segmentedSteps( polymer, instructions, count):
    segments = {}
    for i in range(1, len(polymer)):
        curr = ''.join(polymer[i-1:i+1])
        #segments[curr] = 1
        if curr in segments:
            segments[curr] += 1
        else:
            segments[curr] = 1
    for i in range(0, count):
        segments = segmentedStep(segments, instructions)
    return segments

def quantities(polymer):
    quant = {}
    for p in polymer:
        if p in quant:
            quant[p] += 1
        else:
            quant[p] = 1
    return quant

def douQuantToQuant(douQuant, last):
    quant = {}
    for p in douQuant:
        if p[0] in quant:
            quant[p[0]] += douQuant[p]
        else:
            quant[p[0]] = douQuant[p]
    if last in quant:
        quant[last] += 1
    else:
        quant[last] = 1
    return quant

def printQuantStats(quant):
    key_max = max(quant.keys(), key=(lambda k: quant[k]))
    key_min = min(quant.keys(), key=(lambda k: quant[k]))
    print('Diff Value: ', quant[key_max]-quant[key_min])

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

start, instructions = readValues(file_path)
start_time = time.time()

print(''.join(start))

douQuant = segmentedSteps(start.copy(), instructions, 40)
#print(douQuant)
quant = douQuantToQuant(douQuant, start[-1])
print(quant)
printQuantStats(quant)

end_time = time.time()
print("time:", end_time - start_time)