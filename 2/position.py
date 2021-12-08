#!/usr/bin/python
import io
import os

def readMoves(file_path):
    file_in = open(file_path, 'r')
    moves = []
    for line in file_in:
        split_line = line.split(' ')
        move = [0, 0]
        v = int(split_line[1])
        if split_line[0] == 'forward':
            move[0] = v
        elif split_line[0] == 'down':
            move[1] = v
        elif split_line[0] == 'up':
            move[1] = -v
        moves.append(move)

    file_in.close()
    return moves

def movePoint(moves):
    position = [0,0]
    for move in moves:
        position[0] += move[0]
        position[1] += move[1]
    return position

def moveBoot(file_path):
    file_in = open(file_path, 'r')
    position = [0, 0]
    aim = 0

    for line in file_in:
        split_line = line.split(' ')
        #print(split_line)

        v = int(split_line[1])
        if split_line[0] == 'forward':
            position[0] += v
            position[1] += aim*v
        elif split_line[0] == 'down':
            aim += v
        elif split_line[0] == 'up':
            aim -= v

    file_in.close()
    return position

path = os.path.dirname(__file__)

file_path = os.path.join(path, "input.txt")
moves = readMoves(file_path)
position = movePoint(moves)

print("x:", position[0], " y:", position[1])
print("p:", position[0]*position[1])

file_path = os.path.join(path, "test.txt")
position = moveBoot(file_path)
print("x:", position[0], " y:", position[1])
print("p:", position[0]*position[1])

file_path = os.path.join(path, "input.txt")
position = moveBoot(file_path)
print("x:", position[0], " y:", position[1])
print("p:", position[0]*position[1])
