#!/usr/bin/python
import io
import os

def is_set(x, n):
    return (x & (1 << n)) != 0

def set_bit(x, n):
    return x | (1<<n)

def readValues(file_path):
    print("read file:", file_path)
    file_in = open(file_path, 'r')
    values = []
    for line in file_in:
        v = int(line, 2)
        values.append(v)
        #print(v)

    file_in.close()
    print("read count:", len(values))
    return values

def countBit(values, bit):
    count = 0
    for v in values:
        if is_set(v, bit):
            count += 1
    return count

def power(values, r):
    ones = [0]*r

    for i in range(r):
        ones[i] = countBit(values, i)

    print("bit count:", ones)

    gamma = 0
    epsilon = 0
    half = len(values) >> 1

    for i in range(r):
        if ones[i] > half:
            gamma = set_bit(gamma, i)
        else:
        #elif ones[i] < half:
            epsilon = set_bit(epsilon, i)
    
    return [gamma, epsilon]

def lifeSupport(values, bit_count, less):

    filtered_list = values

    for i in reversed(range(bit_count)):
        half = len(filtered_list)*0.5
        bit_count = countBit(filtered_list, i)
        next_list = []

        if less:
            check_set = bool(bit_count < half)
        else:
            check_set = bool(bit_count >= half)

        for v in filtered_list:
            if check_set:
                if is_set(v, i) == 1:
                    next_list.append(v)
                    #print("append :", v, "|", bin(v))
            else:
                if is_set(v, i) == 0:
                    next_list.append(v)
                    #print("append :", v, "|", bin(v))
        filtered_list = next_list
        if len(filtered_list) == 1:
            break
    return filtered_list[0]

path = os.path.dirname(__file__)

file_path = os.path.join(path, "test.txt")
values = readValues(file_path)
[gamma, epsilon] = power(values, 5)

print("gamma:", gamma)
print("eps:", epsilon)
print("prod:", gamma*epsilon)

oxy = lifeSupport(values, 5, False)
co2 = lifeSupport(values, 5, True)
print("oxy:", oxy)
print("co2:", co2)

file_path = os.path.join(path, "input.txt")
values = readValues(file_path)
[gamma, epsilon] = power(values, 12)

print("gamma:", gamma)
print("eps:", epsilon)
print("prod:", gamma*epsilon,"\n")

oxy = lifeSupport(values, 12, False)
co2 = lifeSupport(values, 12, True)
print("oxy:", oxy)
print("co2:", co2)
print("prod:", oxy*co2)