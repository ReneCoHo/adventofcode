"""
- solution based on NOTES.md file, Approach #2,
- second approach after getting stuck with cognitive load of managing circuits,
- using DSU (Disjoint Set Union) data structure to manage circuits

- Solving Part 2
"""
from dataclasses import dataclass
from typing import List, Tuple
from itertools import combinations
from math import dist, prod
from pathlib import Path

script_dir = Path(__file__).parent
# A 40
# B 25272
file_path = script_dir / "test.txt"
# A 115885
# B 274150525
file_path = script_dir / "input.txt"

type Point = Tuple[int, int, int]

def load(file_path: str) -> List[Point]:
    _boxes = []

    with open(file_path) as f:
        for row in f:
            x, y, z = map(int, row.strip().split(','))
            _boxes.append((x, y, z))

    return _boxes

class DSU:
    def __init__(self, elements=None):
        """
        elements: optional iterable of initial elements
        """
        self.parent = {}
        self.rank = {}
        # PUZZLE SPECIFIC:
        self.size = {item: 1 for item in elements} if elements is not None else {}

        # Initially each element is its own parent (self root)
        if elements is not None:
            for x in elements:
                self.parent[x] = x
                self.rank[x] = 0

    def find(self, x):
        # lazy initialization for unseen elements
        # due to puzzle specific usage od self.size below not work properly

        # if x not in self.parent:
        #     self.parent[x] = x
        #     self.rank[x] = 0
        #     return x

        # GOTCHA: path compression -> flattening the tree
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        # Why do I need union by rank?
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            # PUZZLE SPECIFIC:
            self.size[ry] += self.size[rx]
            del self.size[rx]
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
            # PUZZLE SPECIFIC:
            self.size[rx] += self.size[ry]
            del self.size[ry]
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
            self.size[rx] += self.size[ry]
            del self.size[ry]

        return True


def main():
    boxes: List[Point] = load(file_path)

    data = sorted(combinations(boxes, 2), key=lambda pair: dist(*pair))

    dsu = DSU(elements=boxes)

    number_of_unions = 20_000 # 10 for test input, 1000 for real input

    for box1, box2 in data[:number_of_unions]:
        if dsu.union(box1, box2):
            lastBox1 = box1
            lastBox2 = box2

    # How to count len of disjoint sets?
    # Answer: dsu.size keeps track of sizes of each disjoint set

    res = prod(sorted(dsu.size.values(), reverse=True)[:3])

    print(f"Result: {res}")
    # assert res == 40 # expected for test input

    print("Last union product:", lastBox1[0]*lastBox2[0])

if __name__ == '__main__':
    main()