#!/usr/bin/env python
import time

file_path = "D:\\develop\\personal\\AoC\\2025\\1\\input.txt"

def read(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()

    actions=[]
    for line in lines:
        number = int(line[1:])
        rot = line[0]

        if rot == 'L':
            actions.append(-number)
        else:
            actions.append(number)

    return actions

def check_zero(data)->int:
    count=0
    pos=50
    for rot in data:
        pos = (pos + rot) % 100
        if pos == 0:
            count+=1

    return count

def reduce(data):
    red_data=[]
    sum=data[0]

    for rot in data[1:]:
        if rot <= 0 and sum <= 0 :
            sum +=rot
            continue
        elif rot >= 0 and sum >= 0 :
            sum +=rot
            continue
        else:
            red_data.append(sum)
            sum=rot
    
    red_data.append(sum)

    return red_data

def zero_crossing1(data)->int:
    count=0
    position=50

    for rot in data:
        for _ in range(abs(rot)):
            if rot > 0:
                position+=1
            elif rot < 0:
                position-=1

            position = position % 100
            if position == 0:
                count += 1
    return count

def zero_crossing2(data)->int:
    count=0
    position=50

    for rot in data:
        sign = bool(position > 0)
        position = position + rot
        count += int(abs(position/100))

        if sign and position <= 0:
            count += 1

        position = position % 100

    return count

data = read(file_path)
print("check zero:", check_zero(data))
start = time.time()
print("zero crossing 1:", zero_crossing1(data))
end = time.time()
print(f"Time1: {end - start:.4f} second")

start = time.time()
data = reduce(data)
print("zero crossing 2", zero_crossing2(data))
end = time.time()
print(f"Time2: {end - start:.4f} second")
