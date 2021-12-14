#!/usr/bin/python
import io
import os

#https://pypi.org/project/networkx/
#https://networkx.org/documentation/latest/_downloads/networkx_reference.pdf
import networkx as nx
import matplotlib.pyplot as plt

def readGraph(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    G = nx.Graph()
    for line in lines:
        knots = line.rstrip().split('-')
        G.add_node(knots[0], big = knots[0].isupper())
        G.add_node(knots[1], big = knots[1].isupper())
        G.add_edge(knots[0], knots[1])
    return G

def searchPath(G, curr, target, use_knots, path, pathes, doubleUse):
    curr_path = path.copy()
    curr_path.append(curr)  
    if curr == target:
        pathes.append(curr_path)
        return

    curr_used = use_knots.copy()
    curr_used.add(curr)
    for next in G.neighbors(curr):
        if next == "start":
            continue
        if G.nodes[next]["big"] or not next in curr_used:
            searchPath(G, next, target, curr_used, curr_path, pathes, doubleUse)
        elif not doubleUse:
            searchPath(G, next, target, curr_used, curr_path, pathes, True)
    return

def pathCollector(G, source, target):
    pathes = []
    use_knots = set()
    use_knots.add(source)
    path = [source]
    for next in G.neighbors(source):
        searchPath(G, next, target, use_knots, path, pathes, False)

    return pathes

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
#file_path = os.path.join(path, "test2.txt")
#file_path = os.path.join(path, "test3.txt")
file_path = os.path.join(path, "input.txt")

G = readGraph(file_path)

simple_list = nx.all_simple_paths(G, source="start", target="end", cutoff=None)
#sum = 0
#for path in simple_list:
    #print(path)
    #sum += 1
#print("simple count", sum)

pathes = pathCollector(G, source="start", target="end")
print("p count", len(pathes))
#for path in pathes:
#    print(path)

#print(list(G.nodes(data=True)))
#adj = {n:nbrdict for n, nbrdict in G.adjacency()}
#print(adj)

#A = nx.adjacency_matrix(G)
#print(A.todense())

nx.draw(G, pos=nx.circular_layout(G), node_color="magenta", edge_color="blue", with_labels=True)
plt.show()
