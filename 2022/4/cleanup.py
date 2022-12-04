#!/usr/bin/python
import os


def totalOverlapping(lines):
    count=0
    for line in lines:
        intervals = line.rstrip().split(',')
        A = list(map(int, intervals[0].split('-')))
        B = list(map(int, intervals[1].split('-')))
        if A[0] <= B[0] and B[0] <= A[1] and A[0] <= B[1] and B[1] <= A[1]:
            count+=1
        elif B[0] <= A[0] and A[0] <= B[1] and B[0] <= A[1] and A[1] <= B[1]:
            count+=1

    return count

def overlapping(lines):
    count=0
    for line in lines:
        intervals = line.rstrip().split(',')
        A = list(map(int, intervals[0].split('-')))
        B = list(map(int, intervals[1].split('-')))
        if (A[0] <= B[0] and B[0] <= A[1]) or (A[0] <= B[1] and B[1] <= A[1]):
            count+=1
        elif (B[0] <= A[0] and A[0] <= B[1]) or (B[0] <= A[1] and A[1] <= B[1]):
            count+=1

    return count

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    lines = f.readlines()

print("total overlapping:", totalOverlapping(lines))
print("overlapping:", overlapping(lines))