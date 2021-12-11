#!/usr/bin/python
import io
import os

def readValues(file_path):
    file_in = open(file_path, 'r')
    segment_lines = []
    for line in file_in:
        line_parts = line.rstrip().split('|')
        line_inputs = line_parts[0].rstrip().split(' ')
        line_outputs = line_parts[1].lstrip().split(' ')
        line_inputs = [''.join(sorted(part)) for part in line_inputs]
        line_outputs = [''.join(sorted(part)) for part in line_outputs]
        segment_lines.append([line_inputs, line_outputs])

    file_in.close()
    print("read count:", len(segment_lines))
    return segment_lines

def countDigits(field, bits):
    count = 0
    print("len",len(field))
    for line in field:
         for f in line[1]:
            for b in bits:
                if len(f) == b:
                    count += 1
    return count

def figureToBits(figures):
    bits = []
    for f in figures:
        if f == 0:
            b = 6
        elif f == 1:
            b = 2
        elif f == 2 or f == 3 or f == 5:
            b = 5
        elif f == 4 :
            b = 4
        elif f == 6 or f == 9:
            b = 6    
        elif f == 7 :
            b = 3
        elif f == 8 :
            b = 7
        bits.append(b)
    return bits

def compareLetter(a,b):
    for l in a:
        if not l in b:
            return False
    return True

def createDic(input):
    input.sort(key=len)
    #print("input:", input)
    str_fig = {}
    f_str = {}
    str_fig[input[0]] = 1
    str_fig[input[1]] = 7
    str_fig[input[2]] = 4
    str_fig[input[9]] = 8

    f_str[1] = input[0]
    f_str[7] = input[1]
    f_str[4] = input[2]
    f_str[8] = input[9]

    # 3, 4, 5 -> 5 bits
    # 6, 7, 8 -> 6 bits
    for i in range(3, 6):
        if compareLetter(f_str[1], input[i]):
            f_str[3] = input[i]
            str_fig[input[i]] = 3

    for i in range(6, 9):
        if not compareLetter(f_str[1], input[i]):
            f_str[6] = input[i]
            str_fig[input[i]] = 6
        elif compareLetter(f_str[3], input[i]):
            f_str[9] = input[i]
            str_fig[input[i]] = 9
        else :
            f_str[0] = input[i]
            str_fig[input[i]] = 0
    for i in range(3, 6):
        if f_str[3] == input[i]:
            continue
        if compareLetter(input[i], f_str[9]):
            f_str[5] = input[i]
            str_fig[input[i]] = 5
        else : 
            f_str[2] = input[i]
            str_fig[input[i]] = 2
    return str_fig

def translate(data, dic):
    return [dic.get(d) for d in data]

def interpreteAll(segment_lines):
    total_sum = 0
    for input in segment_lines:
        dic = createDic(input[0])
        #print(dic)
        parsed_output = translate(input[1], dic)
        #print(parsed_output)
        number = 0
        for i in range(0, len(parsed_output)):
            f = parsed_output[i]
            number += f*pow(10, len(parsed_output)-1-i)
        #print("n", number)
        total_sum += number

    return total_sum

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "test2.txt")
file_path = os.path.join(path, "input.txt")
segment_lines = readValues(file_path)

#print("inputs:", segment_lines)
#bits = figureToBits([1,4,7,8])
#print("bits:", bits)
#print("count", countDigits(segment_lines, bits))
#print("")

sum = interpreteAll(segment_lines)
print("sum:", sum)