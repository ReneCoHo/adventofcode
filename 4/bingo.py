#!/usr/bin/python
import io
import os

def readInput(file_path):

    with open(file_path) as f:
        lines = f.readlines()

    lines = [s.rstrip() for s in lines if s.rstrip()]

    data = lines[0].split(',')
    data = [int(v) for v in data]
    print(data)

    fields = []
    for i in range(1, len(lines), 5):

        field = []
        for j in range(5):
            line = lines[i+j].rstrip()
            line_strings = line.split(' ')
            line_strings = [int(s) for s in line_strings if s]
            field.append(line_strings)
        #print(field)
        fields.append(field)

    return [fields, data]

def sumUnmarked(field, marked):
    sum = 0
    for i in range(5):
        for j in range(5):
            if marked[i][j]:
                continue
            sum += field[i][j]
    return sum

def checkBingo(marked):
    for i in range(5):
        sumj = 0
        for j in range(5):
            if marked[i][j]:
                sumj += 1
        if sumj == 5:
            return True
    for j in range(5):
        sumi = 0
        for i in range(5):
            if marked[i][j]:
                sumi += 1
        if sumi == 5:
            return True
    return False        

def createMarkes(n):
    m = []
    for i in range(n):
        mf = []
        for j in range(5):
            mf.append([False, False, False, False, False])
        m.append(mf)
    return m

def markNumber(field, mark, number):
    for i in range(5):
        for j in range(5):
            if field[i][j] == number:
                mark[i][j] = True
    return mark

def doBingo(data, fields):

    field_count = len(fields)
    field_markes = createMarkes(field_count)
    win_fields = set()

    for d in data:
        for i in range(field_count):
            f = fields[i]
            field_markes[i] = markNumber(f, field_markes[i], d)
            if checkBingo(field_markes[i]):
                win_fields.add(i)
                if len(win_fields) == field_count:
                    return d*sumUnmarked(f, field_markes[i])
    return 0

file_path = os.path.join(os.getcwd(), "input.txt")

[fields, data] = readInput(file_path)

p = doBingo(data, fields)
print("Product:", p)
#print(fields)

