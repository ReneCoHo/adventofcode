#!/usr/bin/python
import io
import os
import sys

#https://numpy.org/install/
import numpy as np
#https://pypi.org/project/point2d/#description
from point2d import Point2D

class Line2D:
    """ 2d line"""
    def __init__(self, A, B):
        self.A = A
        self.B = B

def stringToPoint(point_string):
    coord_strings = point_string.split(',')
    x = int(coord_strings[0])
    y = int(coord_strings[1])
    return Point2D (x,y)

def readValues(file_path):
    file_in = open(file_path, 'r')
    values = []
    for line in file_in:
        line_parts = line.rstrip().split(' ')
        if len(line_parts) != 3 :
            # skip
            #sys.exit("wrong input")
            continue
        A = stringToPoint(line_parts[0])
        B = stringToPoint(line_parts[2])
        values.append(Line2D(A, B))
        #print(A.x, "|", A.y, "->", B.x, "|", B.y)

    file_in.close()
    print("read count:", len(values))
    return values

def drawLines(field, lines):

    for line in lines:
            px = line.A.x
            py = line.A.y
            cx = abs(line.A.x - line.B.x)
            cy = abs(line.A.y - line.B.y)
            count = max(cx, cy)
            if line.A.x < line.B.x:
                dx = 1
            elif line.A.x == line.B.x:
                dx = 0
            else:
                dx = -1

            if line.A.y < line.B.y:
                dy = 1
            elif line.A.y == line.B.y:
                dy = 0
            else:
                dy = -1
            for i in range(0, count+1, 1):
                field[py][px] += 1 
                px+=dx
                py+=dy

    return

def countOverlaps(field):
    shape = np.shape(field)
    count = 0
    for x in np.nditer(field):
        if x > 1:
            count += 1
    return count

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")
lines = readValues(file_path)
field = np.zeros([1000, 1000])
#print(field)

drawLines(field, lines)
#print(field)

overlaps = countOverlaps(field)
print("overlaps:", overlaps)
