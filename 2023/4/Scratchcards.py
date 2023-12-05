#!/usr/bin/python
import os
import numpy as np

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

def filter_ints(txt):
    return True if txt.isdigit() else False

def readInput(lines):
    win = [] 
    play = []
    for line in lines:
        line = line.split(": ")[1]
        all_fig = line.split(" | ")
        t = all_fig[0].split(' ')
        t = list(filter(filter_ints, t))
        win.append({int(x) for x in t})

        t = all_fig[1].split(' ')
        t = list(filter(filter_ints, t))
        play.append([int(x) for x in t])
    return win, play

def gamePoints(win, play):
    points = []
    for i, game in enumerate(play):
        game_points = 0
        for g in game:
            if g in win[i]:
                if game_points:
                    game_points *= 2
                else:
                    game_points += 1
        points.append(game_points)

    return points
with open(file_path) as f:
    lines = f.read().splitlines()

win, play = readInput(lines)

points = gamePoints(win, play)
print("1 sum:", np.array(points).sum())

cards = [1]*len(points)

for i, p in enumerate(points):
    if p > 0:
        c = int(np.log2(p) + 1) # calc back from point to cards
        for j in range(c):
            cards[i+j+1] += cards[i]

print("2 sum:", np.array(cards).sum())