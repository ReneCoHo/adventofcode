#!/usr/bin/python
import os
import math
from bitstring import BitArray

def readValues(file_path):
    print("read file:", file_path)
    file_in = open(file_path, 'r')

    #read hex values as string
    hex_text = file_in.readline().rstrip().strip()
    file_in.close()
    return BitArray(hex=hex_text).bin

def parsePackage(bits, length, depth, packet_count):
    #print("depth:", depth)
    i = 0
    pack_ver_sum = 0
    r_packets = 0
    values = []
    while i < length and r_packets < packet_count:
        if 10 + i >= length:
            break

        vers = int(bits[i:i+3], 2)
        i += 3
        id = int(bits[i:i+3], 2)
        i += 3
        r_packets += 1
        pack_ver_sum += vers
        if id == 4:
            #literal
            number = 0
            last = False
            while i < length and not last:
                last = bits[i:i+1] == "0"
                group = int(bits[i+1:i+5], 2)
                number <<= 4
                number += group
                #print("number", number)
                i += 5
            values.append(number)
            #print("literal id num", id, number)
            #i += 4 - i%4 # padding
        else:
            #print("operator", id)
            l_id = int(bits[i:i+1])
            i+=1
            if l_id == 0:
                pack_length = int(bits[i:i+15], 2)
                i+=15
                #print("pack_length", pack_length)
                readed, ver_sum, sub_values = parsePackage(bits[i:], pack_length, depth+1, math.inf)
                pack_ver_sum += ver_sum
            else:
                pack_count = int(bits[i:i+11], 2)
                i+=11
                #print("pack_count", pack_count)
                readed, ver_sum, sub_values = parsePackage(bits[i:], len(bits[i:]), depth+1, pack_count)
                pack_ver_sum += ver_sum

            i += readed

            if id == 0:
                #print("sum", sub_values)
                values.append(sum(sub_values))
            elif id == 1:
                #print("prod", sub_values)
                p = 1
                for v in sub_values:
                    p*=v
                values.append(p)
            elif id == 2:
                #print("min", depth, sub_values)
                values.append(min(sub_values))
            elif id == 3:
                #print("max", sub_values)
                values.append(max(sub_values))
            elif id == 5:
                #print("gr", sub_values)
                if sub_values[0]>sub_values[1]:
                    values.append(1)
                else:
                    values.append(0)
            elif id == 6:
                #print("le", sub_values)
                if sub_values[0]<sub_values[1]:
                    values.append(1)
                else:
                    values.append(0)
            elif id == 7:
                #print("eq", sub_values)
                if sub_values[0]==sub_values[1]:
                    values.append(1)
                else:
                    values.append(0)

    print("pack values:", i, pack_ver_sum, values)
    return i, pack_ver_sum, values

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "test2.txt")
#file_path = os.path.join(path, "test3.txt")
#file_path = os.path.join(path, "test4.txt")
file_path = os.path.join(path, "input.txt")

bits = readValues(file_path)
print("len", len(bits))
#print("bits:", bits)

print("read ver sum", parsePackage(bits, len(bits), 0, math.inf))