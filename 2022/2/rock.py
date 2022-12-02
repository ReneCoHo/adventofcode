#!/usr/bin/python
import os

shape_pts = {'A': 0, 'B' : 1, 'C' : 2, 'X' : 0, 'Y' : 1, 'Z' : 2}

pmat = [[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]

smat = [[3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]]

st_mat = [[3, 1, 2],
          [4, 5, 6],
          [8, 9, 7]]


def first(lines):
    total_points = 0
    for line in lines:
        shapes = line.rstrip().split(' ')
        pos = [shape_pts[shapes[0]], shape_pts[shapes[1]]]
        total_points += pmat[pos[0]][pos[1]]
        total_points += smat[pos[0]][pos[1]]
    return total_points

def second(lines):
    total_points = 0
    for line in lines:
        shapes = line.rstrip().split(' ')
        pos = [shape_pts[shapes[0]], shape_pts[shapes[1]]]
        total_points += st_mat[pos[1]][pos[0]]
    return total_points  

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    lines = f.readlines()

print("first:", first(lines))
print("second:", second(lines))