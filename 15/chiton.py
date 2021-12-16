#!/usr/bin/python
import os

#https://pypi.org/project/networkx/
#https://networkx.org/documentation/latest/_downloads/networkx_reference.pdf
import networkx as nx
import matplotlib.pyplot as plt
from pandas import *

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    # get array
    values = []
    for line in lines:
        knot_line = line.rstrip()
        values.append([int(c) for c in knot_line])

    return values

def createGraph(field):
    G = nx.DiGraph()
    for y in range(len(field)):
        for x in range(len(field[y])):
            kyx = str(y) + "_" + str(x)
            ky1x = str(y+1) + "_" + str(x)
            kyx1 = str(y) + "_" +  str(x+1)
            G.add_node(kyx)
            if y+1 < len(field):
                G.add_node(ky1x)
                G.add_edge(kyx, ky1x, weight = field[y+1][x])
                G.add_edge(ky1x, kyx, weight = field[y][x])
            if x + 1 < len(field[y]):
                G.add_node(kyx1)
                G.add_edge(kyx, kyx1, weight = field[y][x+1])
                G.add_edge(kyx1, kyx, weight = field[y][x])
    return G

def multiField(field, factor):
    sy = len(field)
    sx = len(field[0])
    fac_field = [[0 for x in range(sy*factor)] for y in range(sy*factor)]

    for i in range(factor):
        for j in range(factor):
            for y in range(sy):
                for x in range(sx):
                    f = (field[y][x] + i + j - 1)%9
                    fac_field[y+j*sy][x+i*sx] = f + 1
    return fac_field

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

field = readValues(file_path)
field = multiField(field, 5)

print(len(field), "x", len(field[0]))
#print(DataFrame(field))

G = createGraph(field)
#nx.draw(G, pos=nx.circular_layout(G), node_color="magenta", edge_color="blue", with_labels=True)
#plt.show()
ys = len(field)-1
xs = len(field[0])-1
tar = str(ys) + "_" + str(xs)
start = "0_0"
print("from", start, "to:", tar )
simple_list = nx.dijkstra_path(G, source=start, target=tar, weight='weight')
#print(simple_list)

sum = 0

for i in range(len(simple_list)-1):
    w = G[simple_list[i]][simple_list[i+1]]["weight"]
    sum += w

print("sum:", sum)