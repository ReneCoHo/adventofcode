import numpy as np
from pathlib import Path

script_dir = Path(__file__).parent
# 4277556, 3263827
file_path = script_dir / "test.txt"
# 7098065460541, 13807151830618
file_path = script_dir / "input.txt"

def read(file_path):
    figures = []
    operations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            line = line.strip()
            entitys = line.split()
            figures.append([int(e) for e in entitys])
        line = lines[-1].strip()
        operations = line.split()

    return figures, operations

def read_cephal(file_path):
    operations = []
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    operations = lines.pop().split()
    return lines, operations

def calcluate_operations(figures, operations):
    np_figures = np.array(figures)
    results = []
    for index, op in enumerate(operations):
        if op == "+":
            r = 0
            for f in np_figures[:, index]:
                r+=f
        else:
            r = 1
            for f in np_figures[: ,index]:
                r*=f
        results.append(r)
    return results

# def transform_numbers(numbers):
#     ceph_numbers=np.array(dtype=int)
#     while True:
#         n=0
#         digit=0
#         for f in numbers:
#             str(f)
#             n= n*10 + 
#         ceph_numbers.append(n)
#     return ceph_numbers

def calcluate_digit_operations(lines, operations):
    results = []

    o = 0
    c = 0
    while c < len(lines[1]):
        op = operations[o]
        if op == "+":
            r = 0
        else:
            r = 1
        while c < len(lines[1]):
            d = ""
            for l in lines:
                if not l[c] ==" ":
                    d += l[c]
            c += 1
            if d:
                f = int(d)
                if op == "+":
                    r+=f
                else:
                    r*=f
            else:
                break
        results.append(r)
        o += 1
        
    return results

figures, operations = read(file_path)
results = calcluate_operations(figures, operations)
print("operation sum:", sum(results))

lines, operations = read_cephal(file_path)
results = calcluate_digit_operations(lines, operations)
print("cephal sum:", sum(results))
