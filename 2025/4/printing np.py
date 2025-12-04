#!/usr/bin/env python
import numpy as np
import time
from scipy.ndimage import convolve
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
def read(file_path) -> np.array :
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    diagram = np.array([[1 if c == "@" else 0 for c in line] for line in lines])
    return diagram

def count_less_neighbors(diagram, max_neighbors : int) -> int:
    kernel = np.ones((3,3), dtype=int)
    kernel[1,1] = 0  # ignore center
    neighbor_counts = convolve(diagram, kernel, mode='constant', cval=0)
    isolated = (diagram == 1) & (neighbor_counts < 4)
    return isolated.sum()

def remove_less_neighbors(diagram, max_neighbors : int) -> int:
    kernel = np.ones((3,3), dtype=int)
    kernel[1,1] = 0  # ignore center
    changed = True
    removed_count = 0
    while changed:
        neighbor_counts = convolve(diagram, kernel, mode='constant', cval=0)
        isolated = (diagram == 1) & (neighbor_counts < 4)
        s = isolated.sum()
        changed = s > 0
        removed_count += s
        diagram[isolated] = 0
    return removed_count

if __name__ == "__main__":
    diagram = read(file_path)
    start = time.time()
    count = count_less_neighbors(diagram, 4)
    print("Rolls count:", count)

    removed = remove_less_neighbors(diagram, 4)
    print("Rolls removed:", removed)
    end = time.time()
    print(f"Time: {end - start:.4f} second")