#!/usr/bin/env python
from typing import List
from pathlib import Path

script_dir = Path(__file__).parent

#13, 43
file_path = script_dir / "test.txt"
#1416, 9086
file_path = script_dir / "input.txt"

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1), 
    (0, -1),           (0, 1), 
    (1, -1),  (1, 0),  (1, 1) 
]

# ============ functions ============ 

def read(file_path) -> List[List[int]] :
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    diagram = [[1 if c == "@" else 0 for c in line] for line in lines]
    return diagram

def count_neighbors(diagram : List[List[int]], row : int, col : int) -> int:
    """count one in 8 neighbor"""
    rows = len(diagram)
    cols = len(diagram[0]) if rows > 0 else 0

    n_count = 0
    for dr, dc in DIRECTIONS:
        new_row = row + dr
        new_col = col + dc

        # check border
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if diagram[new_row][new_col] == 1:
                n_count += 1
    
    return n_count

def count_less_neighbors(diagram : List[List[int]], max_neighbors : int):
    less_count=0
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] == 1:
                count = count_neighbors(diagram, row, col)
                if count < max_neighbors:
                    less_count+=1
    return less_count

def remove_rolls(diagram : List[List[int]], max_neighbors : int) -> int:
    total_removed = 0
    changed = True
    while changed:
        changed = False

        for row in range(len(diagram)):
            for col in range(len(diagram[0])):
                if diagram[row][col] == 1:
                    if count_neighbors(diagram, row, col) < max_neighbors:
                        total_removed += 1
                        diagram[row][col] = 0
                        changed = True

    return total_removed

if __name__ == "__main__":
    diagram = read(file_path)
    count = count_less_neighbors(diagram, 4)
    print("Rolls count:", count)
    removed = remove_rolls(diagram, 4)
    print("Rolls removed:", removed)