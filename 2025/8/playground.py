import numpy as np
import scipy
from pathlib import Path

script_dir = Path(__file__).parent
# 10 -> 40
file_path = script_dir / "test.txt"
# 1000 -> 
#
# file_path = script_dir / "input.txt"

def read(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    positions = [line.split(',') for line in lines]
    return np.array(positions)

def connect(edges_sorted, p):
    c_count = 0
    connected = set()
    junctions = [x for x in range(len(p))]
    for e in edges_sorted:
        if c_count==10:
            break
        a = int(e[0])
        b = int(e[1])
        cedge = tuple(sorted([a, b]))
        if cedge in connected:
            continue 
        if junctions[a] == junctions[b]:
             continue
        c_count += 1
        dest = junctions[a]
        tar = junctions[b]
        connected.add(cedge)
        #print("connect:", p[int(e[0])], p[int(e[1])])
        for i, j in enumerate(junctions):
            if j == tar:
                junctions[i] = dest

    return junctions

def product(junctions, n)->int:
    # count
    j_sizes=[0 for _ in range(n)]
    for j in junctions:
        j_sizes[j] += 1

    sj_sizes = sorted(j_sizes, reverse=True)
    return sj_sizes[0]*sj_sizes[1]*sj_sizes[2]

def calculate_edges(positions):
    position_tree = scipy.spatial.KDTree(positions)

    print("shape:", positions.shape)
    edges = []

    for i_p, item in enumerate(positions):
        # dd, ii = position_tree.query(item, k=[2], distance_upper_bound=1000)
        dd, ii = position_tree.query(item, k=30, distance_upper_bound=100000)
        #print(dd, ii, sep='\n')
        for i_d, d in enumerate(dd):
            if d > 0:
                edges.append([int(i_p), int(ii[i_d]), d])
                # if int(i_p) <= int(ii[i_d]):
                # else:
                #     edges.append([int(ii[i_d], int(i_p)), d])
    return np.array(edges)


positions = read(file_path)
edges = calculate_edges(positions)
#edges_sorted = sorted(edges, key=lambda x: x[2])
edges_sorted = edges[edges[:, 2].argsort()]
junctions = connect(edges_sorted, positions)
print("result:", product(junctions, len(positions)))
#print(edges_sorted[0])