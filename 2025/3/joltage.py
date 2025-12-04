#!/usr/bin/env python
import time

#file_path = "D:\\develop\\personal\\AoC\\2025\\3\\test.txt"#357, 3121910778619
file_path = "D:\\develop\\personal\\AoC\\2025\\3\\input.txt"#17207, 170997883706617

def read(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    return lines

def calc_2joltage(lines):
    joltage = []
    for line in lines:
        i_l = 0
        l=0
        r=0
        i_r = 0
        for i in range(len(line)-1):
            if int(line[i]) > l:
                l = int(line[i])
                i_l = i

        for i in range(i_l+1, len(line)):
            if int(line[i]) > r:
                r = int(line[i])
                i_r = i
        joltage.append(int(line[i_l]+line[i_r]))
    return joltage

def calc_joltage(lines, digits):
    joltage = []
    for line in lines:
        jol=0
        last_pos=-1

        for ci in range(0, digits):
            last_jol = 0
            for i in range(last_pos+1, len(line) - digits + ci + 1):
                if int(line[i]) > last_jol:
                    last_jol = int(line[i])
                    last_pos = i
                if last_jol==9:
                    break
            jol = 10*jol + last_jol

        joltage.append(jol)
    return joltage

data = read(file_path)

start = time.time()
joltage = calc_2joltage(data)
end = time.time()
print(f"Time1: {end - start:.4f} second")
print("2 joltage sum:", sum(joltage))

start = time.time()
joltage = calc_joltage(data, 12)
end = time.time()
print(f"Time1: {end - start:.4f} second")

print("12 joltage sum:", sum(joltage))
