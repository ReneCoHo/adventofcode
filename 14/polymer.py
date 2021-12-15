#!/usr/bin/python
import io
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

def step2( polymer, instructions):
    polymer_out = []

    for i in range(1, len(polymer)):
        curr = ''.join(polymer[i:i+2])
        polymer_out.append(polymer[i])
        if curr in instructions:
            polymer_out.append(instructions[curr])
        #print("after add", ''.join(polymer_out))
    polymer_out.append(polymer[-1])
    return polymer_out

def step( polymer, instructions):
    i = 1
    while i < len(polymer):
        curr = ''.join(polymer[i-1:i+1])
        #print(i, curr)
        if curr in instructions:
            polymer.insert(i, instructions[curr])
            i += 1
        i += 1
        #print("after add", ''.join(polymer))
    return polymer

def steps( polymer, instructions, count):
    for i in range(0, count):
        #if i%5 == 0:
        #    print("i", i) 
        #polymer = step2(polymer, instructions)
        step(polymer, instructions)
    return polymer

def quantities(polymer):
    quant = {}
    for p in polymer:
        if p in quant:
            quant[p] += 1
        else:
            quant[p] = 1
    return quant

path = os.path.dirname(__file__)
file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "input.txt")

start, instructions = readValues(file_path)
start_time = time.time()

print(start)
print(instructions)

polymer = steps(start, instructions, 17)
#print(''.join(polymer))
print("polymer size:", len(polymer))
quant = quantities(polymer)
print(quant)

key_max = max(quant.keys(), key=(lambda k: quant[k]))
key_min = min(quant.keys(), key=(lambda k: quant[k]))

print('Maximum Value: ', quant[key_max])
print('Minimum Value: ', quant[key_min])
print('Diff Value: ', quant[key_max]-quant[key_min])

end_time = time.time()
print("time:", end_time - start_time)