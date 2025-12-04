#!/usr/bin/env python
import time
import numpy as np

#file_path = "D:\\develop\\personal\\AoC\\2025\\4\\test.txt"#13, 43
file_path = "D:\\develop\\personal\\AoC\\2025\\4\\input.txt"#1416, 9086

def read(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    diagram = [[1 if c == "@" else 0 for c in line] for line in lines]
    return diagram

def count_neighbors(diagram, row, col):
    """count one in 8 neighbor"""
    rows = len(diagram)
    cols = len(diagram[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1),           (0, 1), 
        (1, -1),  (1, 0),  (1, 1) 
    ]

    n_count = 0
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # check border
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if diagram[new_row][new_col] == 1:
                n_count += 1
    
    return n_count

def count_less_neighbors(diagram, neighbors):
    less_count=0
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] == 1:
                count = count_neighbors(diagram, row, col)
                if count < neighbors:
                    less_count+=1
    return less_count

def remove_rolls(diagram, neighbors)->int:
    removed=0
    while True:
        lremoved=removed
        for row in range(len(diagram)):
            for col in range(len(diagram[0])):
                if diagram[row][col] == 1:
                    count = count_neighbors(diagram, row, col)
                    if count < neighbors:
                        removed += 1
                        diagram[row][col] = 0
        if lremoved == removed:
            break

    return removed

diagram = read(file_path)
count = count_less_neighbors(diagram, 4)
print("Rolls count:", count)
removed = remove_rolls(diagram, 4)
print("Rolls removed:", removed)