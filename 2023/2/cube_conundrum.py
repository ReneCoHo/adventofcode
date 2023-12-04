#!/usr/bin/python
import os
import numpy as np

path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

def readGames(lines):
    games = []
    for line in lines:
        line = line.split(":")[1]
        sets = line.rstrip("\n").split(";")
        game = {"green" : 0, "blue" : 0, "red" : 0}
        for set in sets:
            colorStrings = set.split(",")
            for colorString in colorStrings:
                col = colorString.lstrip().split(" ")
                col_count = int(col[0])
                if col[1] in game:
                    if game[col[1]] < col_count:
                        game[col[1]] = col_count
                else:
                    print("miss")

        games.append(game)
    return games

def checkValid(games, set):
    sum=0
    for id in range(len(games)):
        g = games[id]
        valid = True
        for color in g:
            if not color in set:
                valid = False
                break
            elif g[color] > set[color]:
                valid = False
                break
        if valid:
            sum += id+1
    return sum

with open(file_path) as f:
    lines = f.readlines()

set = {"red":12, "green":13, "blue" : 14}
games = readGames(lines)
validSum = checkValid(games, set)

print("1 sum:", validSum)

#values = readNamedDigits(lines)
#print(values)
#print("2 sum:", values.sum())
