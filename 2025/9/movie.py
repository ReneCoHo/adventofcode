import numpy as np
from itertools import combinations
from math import dist
from pathlib import Path
from typing import List, Tuple

script_dir = Path(__file__).parent
# 50
file_path = script_dir / "test.txt"
# 4760959496
#file_path = script_dir / "input.txt"
type Point = Tuple[int, int]

def read(file_path) -> List[Point]:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    positions = [
        [int(x) for x in line.split(',')]
        for line in lines
    ]
    return positions

def area(pair):
    return (1+abs(pair[1][0] - pair[0][0]))*(1+abs(pair[1][1] - pair[0][1]))

def check_red_tiles(pair, positions):
    for p in positions:
        if (pair[0][0] < p[0] and p[0] < pair[1][0]) or (pair[1][0] < p[0] and p[0] < pair[0][0]):
            if (pair[0][1] < p[1] and p[1] < pair[1][1]) or (pair[1][1] < p[1] and p[1] < pair[0][1]):
                return True
    return False

def is_point_in_polygon(p, vertices, points, points_min_x, cache):
    if p in cache:
        return cache[p]
    if p in vertices or p in points:
        return True
    x, y = p
    count = 0
    vertex = None
    while x >= points_min_x - 1:
        if (x, y) in vertices:
            vertex_dir = -1 if (x, y - 1) in points or (x, y - 1) in vertices else 1
            if vertex is None:
                vertex = vertex_dir
            elif vertex != vertex_dir:
                count += 1
                vertex = None
        if (x, y) in points and vertex is None:
            count += 1
        x -= 1
    ret = count % 2 != 0
    cache[p] = ret
    return ret


def is_line_in_polygon(l, vertices, points, points_min_x, cache):
    (x1, y1), (x2, y2) = l

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if min_x == max_x:
        for y in range(min_y, max_y):
            if not is_point_in_polygon(
                (min_x, y), vertices, points, points_min_x, cache
            ):
                return False
    else:
        for x in range(min_x, max_x):
            if not is_point_in_polygon(
                (x, min_y), vertices, points, points_min_x, cache
            ):
                return False

    return True

positions: List[Point] = read(file_path)

data = sorted(combinations(positions, 2), key=lambda pair: area(pair))
# A
print(data[-1])
print(area(data[-1]))

#B
points_min_x = min([p[0] for p in positions])
vertices = set([(p[0], p[1]) for p in positions])
points = set()

for i in range(len(positions)):
    p1 = data[i]
    p2 = data[(i + 1) % len(positions)]
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])
    direction = "h" if min_y == max_y else "v"
    if direction == "h":
        for x in range(min_x + 1, max_x):
            points.add((x, min_y))
    else:
        for y in range(min_y + 1, max_y):
            points.add((min_x, y))

largest = -1

cache = dict()

for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        p1, p3 = positions[i], positions[j]
        (x1, y1), (x2, y2) = p1, p3

        if x1 == x2 or y1 == y2:
            continue
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area < largest:
            continue

        p2, p4 = (x1, y2), (x2, y1)

        lines = [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]

        inside = True
        for line in lines:
            if not is_line_in_polygon(line, vertices, points, points_min_x, cache):
                inside = False
                break

        if inside:
            largest = max(largest, area)

print("lagest", largest)