import numpy as np
from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
# 21, 40
file_path = script_dir / "test.txt"
# 1504, 5137133207830
file_path = script_dir / "input.txt"

def read(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    return lines

def split_tachyon(lines):
    tachyons = {lines[0].find("S")}
    count = 0
    for i in range(2, len(lines), 2):
        next_t = set()
        for t in tachyons:
            if lines[i][t] == "^":
                count +=1
                next_t.add(t-1)
                next_t.add(t+1)
            else:
                next_t.add(t)
        tachyons = next_t
        
    return count

def tachyon_timelines(lines):
    hashtable = defaultdict(int)
    hashtable[lines[0].find("S")] = 1
    width = len(lines[0])

    for i in range(2, len(lines), 2):
        newhashtable = defaultdict(int)
        for x in range(width):
            if lines[i][x] == ".":
                newhashtable[x] += hashtable[x]
                continue
            # split
            newhashtable[x - 1] += hashtable[x]
            newhashtable[x + 1] += hashtable[x]
        hashtable = newhashtable
        
    return sum(hashtable.values())

lines = read(file_path)
count = split_tachyon(lines)
print("tachyon splits:", count)

lines = read(file_path)
count = tachyon_timelines(lines)
print("tachyon timelines:", count)
