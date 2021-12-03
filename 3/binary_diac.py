#!/usr/bin/python
import io
import os

def is_set(x, n):
    return (x & (1 << n)) != 0

def set_bit(x, n):
    return x | (1<<n)

def readValues(file_path):
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

def lifeSupportOxy(values, r):

    oxy_list = values
    for i in reversed(range(r)):
        half = len(oxy_list)*0.5
        bit_count = countBit(oxy_list, i)
        next_list = []
        #print("i:", i, "bit count:", bit_count)
        #print("half:", half)

        for v in oxy_list:
            if bit_count >= half:
                if is_set(v, i) == 1:
                    #print("append 1:", v, "|", bin(v))
                    next_list.append(v)
            elif bit_count < half:
                if is_set(v, i) == 0:
                    #print("append 0:", v, "|", bin(v))
                    next_list.append(v)
        oxy_list = next_list
        if len(oxy_list) == 1:
            break

    print("len", len(oxy_list))
    v = oxy_list[0]
    print("oxy ", v, "|", bin(v))
    return v

def lifeSupportCO2(values, r):

    co2_list = values
    for i in reversed(range(r)):
        half = len(co2_list)*0.5
        bit_count = countBit(co2_list, i)
        next_list = []
        #print("i:", i, "bit count:", bit_count)
        #print("half:", half)

        for v in co2_list:
            if bit_count >= half:
                if is_set(v, i) == 0:
                    #print("append 1:", v, "|", bin(v))
                    next_list.append(v)
            elif bit_count < half:
                if is_set(v, i) == 1:
                    #print("append 0:", v, "|", bin(v))
                    next_list.append(v)
        co2_list = next_list
        if len(co2_list) == 1:
            break

    print("len", len(co2_list))
    v = co2_list[0]
    print("co2 ", v, "|", bin(v))

    return v

file_path = os.path.join(os.getcwd(), "test.txt")
values = readValues(file_path)
[gamma, epsilon] = power(values, 5)

print("gamma:", gamma)
print("eps:", epsilon)
print("prod:", gamma*epsilon)

oxy = lifeSupportOxy(values, 5)
print("oxy:", oxy)

co2 = lifeSupportCO2(values, 5)
print("co2:", co2)

file_path = os.path.join(os.getcwd(), "input.txt")
values = readValues(file_path)
[gamma, epsilon] = power(values, 12)

print("gamma:", gamma)
print("eps:", epsilon)
print("prod:", gamma*epsilon)

oxy = lifeSupportOxy(values, 12)
print("oxy:", oxy)

co2 = lifeSupportCO2(values, 12)
print("co2:", co2)
print("prod:", oxy*co2)