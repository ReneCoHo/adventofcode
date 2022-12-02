#!/usr/bin/python
import os
from scipy.spatial.transform import Rotation as R
import numpy as np

def readValues(file_path):
    file_in = open(file_path, 'r')
    scanner = []
    for line in file_in:
        if "scanner" in line:
            scanner.append([])
            continue
        if not line.rstrip():
            continue
        pt_str = line.rstrip().split(',')
        scanner[-1].append([int(c) for c in pt_str])
    return scanner

def tryMerge(glob_points, points):
    
    for pt in points:
        for gl_pt in glob_points:
            trans = [gl_pt[0] - pt[0], gl_pt[1] - pt[1], gl_pt[2] - pt[2]]
            new_points = []
            match_point_count = 0
            for curr_pt in points:
                t_pt = [trans[0] + curr_pt[0], trans[1] + curr_pt[1], trans[2] + curr_pt[2]]
                if t_pt in glob_points:
                    match_point_count += 1
                else:
                    new_points.append(t_pt)
            if match_point_count > 11:
                return trans, new_points
    return None, []

def rotate(R, points):
    rPoints= []
    for pt in points:
        r_pt = [
                int(R[0][0]*pt[0] + R[0][1]*pt[1] + R[0][2]*pt[2]),
                int(R[1][0]*pt[0] + R[1][1]*pt[1] + R[1][2]*pt[2]),
                int(R[2][0]*pt[0] + R[2][1]*pt[1] + R[2][2]*pt[2])]
        rPoints.append(r_pt)
    return rPoints

def RotMat(a,b,g):
    r = R.from_euler('zyx', [a, b, g], degrees=True)
    fmat = r.as_matrix()
    mat = []
    for row in fmat:
        iRow = []
        for v in row:
            iRow.append(int(v))
        mat.append(iRow)
    return mat

def getRotations():
    rots = []
    rots.append(RotMat(  0,   0,   0))
    rots.append(RotMat( 90,   0,   0))
    rots.append(RotMat(180,   0,   0))
    rots.append(RotMat(270,   0,   0))
    rots.append(RotMat(  0,  90,   0))
    rots.append(RotMat( 90,  90,   0))
    rots.append(RotMat(180,  90,   0))
    rots.append(RotMat(270,  90,   0))
    rots.append(RotMat(  0, 180,   0))
    rots.append(RotMat( 90, 180,   0))
    rots.append(RotMat(180, 180,   0))
    rots.append(RotMat(270, 180,   0))
    rots.append(RotMat(  0, 270,   0))
    rots.append(RotMat( 90, 270,   0))
    rots.append(RotMat(180, 270,   0))
    rots.append(RotMat(270, 270,   0))
    rots.append(RotMat(  0,   0,  90))
    rots.append(RotMat( 90,   0,  90))
    rots.append(RotMat(180,   0,  90))
    rots.append(RotMat(270,   0,  90))
    rots.append(RotMat(  0,   0, 270))
    rots.append(RotMat( 90,   0, 270))
    rots.append(RotMat(180,   0, 270))
    rots.append(RotMat(270,   0, 270))
    return rots

def tryTransformMerge(glob_points, points):
    Rotations = getRotations()
    for R_mat in Rotations:
        t_points = rotate(R_mat, points)
        trans, new_points = tryMerge(glob_points, t_points)
        if trans:
            glob_points.extend(new_points)
            return trans, True

    return None, False

def mergeScanner(scanner):
    global_points = scanner[0]
    scanner_positions = {0 : [0,0,0]}
    while len(scanner_positions) != len(scanner):
        for i in range(1, len(scanner)):
            if i in scanner_positions:
                continue
            scanner_pos, merged = tryTransformMerge(global_points, scanner[i])
            if merged:
                print("merged:", i)
                scanner_positions[i] = scanner_pos

    return global_points, scanner_positions

def manhattenDistance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

def maxDistance(points):
    max_dist = -1
    for ka in points:
        for kb in points:
            max_dist = max(manhattenDistance(points[ka],points[kb]), max_dist)
    return max_dist

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

scanner = readValues(file_path)
#print(scanner)

points, scanner_pos = mergeScanner(scanner)
print("global barkes:",len(points))

print(scanner_pos)
print("Distance:", maxDistance(scanner_pos))
