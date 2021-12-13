#!/usr/bin/python
import io
import os

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()
    
    values = [line.rstrip() for line in lines]
    print("read count:", len(values))
    return values

def findWrongSign(line):
    associated  = {'(':')', '[':']', '{':'}', '<':'>'}
    open_stack = []

    for c in line:
        if c in associated:
            open_stack.append(c)
        elif open_stack and associated[open_stack[-1]] == c:
            open_stack.pop()
        else:
            return [c, open_stack]

    return ['', open_stack]

def completeValue(c):
    switcher = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }
    return switcher.get(c, 0)

def errorValue(c):
    switcher = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }
    return switcher.get(c, 0)

def completeLineValue(open_stack):
    if not open_stack:
        return 0

    prod = 0
    for c in reversed(open_stack):
        prod *= 5
        prod += completeValue(c)

    return prod

def checkSyntax(line):
    [c, open_stack] = findWrongSign(line)
    return errorValue(c)

def calculateSyntaxError(lines):
    error = 0
    for line in lines:
        error += checkSyntax(line)
    return error

def completeLines(lines):
    scores = []
    for line in lines:
        [c, open_stack] = findWrongSign(line)
        if c == '':
            scores.append( completeLineValue(open_stack) )

    scores.sort()
    #print("scores", scores)
    return scores[len(scores)>>1]


path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

values = readValues(file_path)
#print(values)
print("error:", calculateSyntaxError(values))
print("complete:", completeLines(values))