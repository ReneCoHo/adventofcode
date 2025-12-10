#!/usr/bin/env python
import time
from pathlib import Path

script_dir = Path(__file__).parent
# 3, 14
file_path = script_dir / "test.txt"
# 611, 345995423801866
file_path = script_dir / "input.txt"


def read(file_path):

    ingredients = []
    ranges = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        ing=False
        for line in lines:
            line = line.strip()
            if not line:
                ing = True
                continue
            if ing:
                ingredients.append(int(line))
            else :
                line_sp = line.split('-')
                ranges.append((int(line_sp[0]),int(line_sp[1])))

    return ranges, ingredients

def fresh_count(ranges, ingredients)->int:
    count = 0
    for i in ingredients:
        for a, b in ranges:
            if a <= i and i <= b :
                count += 1
                break
    
    return count

def merge(a, b, c, d):
    if a > d :
        return None
    if b < c :
        return None
    l = min(a,c)
    r = max(b,d)   
    return (l, r)

def reduce(ranges):
    removed=[]
    for i in range(0, len(ranges)) :
        crr = ranges[i]
        changed = True
        while changed:
            changed = False
            for j in range(i+1, len(ranges)) :
                if j in removed:
                    continue
                mr = merge(crr[0], crr[1], ranges[j][0], ranges[j][1])
                if mr:
                    crr = mr
                    removed.append(j)
                    changed = True
        ranges[i] = crr

    removed.sort()
    for j in reversed(removed):
        ranges.pop(j)
    return ranges

def fresh_in_range_count(ranges)->int:
    count = 0
    for r in ranges:
        count += r[1] - r[0] + 1

    return count


ranges, ingredients = read(file_path)
count = fresh_count(ranges, ingredients)

print("fresh count:", count)

red = reduce(ranges)
count = fresh_in_range_count(red)
print("fresh in range count:", count)