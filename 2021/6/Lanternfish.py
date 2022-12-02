#!/usr/bin/python
import io
import os

def readValues(file_path):
    print("read file:", file_path)
    file_in = open(file_path, 'r')
    values = []
    for line in file_in:
        parts = line.rstrip().split(',')
        values = [int(s) for s in parts if s]

    file_in.close()
    #print(values)
    print("read count:", len(values))
    return values

def convertField(field):
    sum_field = [0]*9
    for f in field:
        sum_field[f] += 1
    return sum_field

def day(field):
    t = field[0]
    for i in range(0, 8):
        field[i] = field[i+1]
    
    field[8] = t
    field[6] += t
    return field

def runDays(field, days):
    for i in range(days):
        field = day(field)
    print("day", days, field)
    return field

def count(field):
    sum = 0
    for f in field:
        sum+=f
    return sum

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

field = readValues(file_path)
sum_field = convertField(field)
print(sum_field)
sum_field = runDays(sum_field, 256)

print(sum_field)
print("count:", count(sum_field))
