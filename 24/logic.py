#!/usr/bin/env python3
import os

instructions = {
    "add": (lambda a, b: int(a+b)),
    "mul": (lambda a, b: int(a*b)),
    "div": (lambda a, b: int(a/b)),
    "mod": (lambda a, b: int(a%b)),
    "eql": (lambda a, b: int(a==b))
}

block_dic = {
    0: (lambda z, w: int(15+w)),
    1: (lambda z, w: int(26*z + w + 16)),
    2: (lambda z, w: int(26*z + w + 4)),
    3: (lambda z, w: int(26*z + w + 14)),
    6: (lambda z, w: int(26*z + w + 1)),
    8: (lambda z, w: int(26*z + w + 3)),
    10: (lambda z, w: int(26*z + w + 5))
}

def readValues(file_path):
    with open(file_path) as f:
        data = f.read()
    blocks = []
    for block in data.split("inp w"):
        if len(block) == 0:
             continue
        block = block.splitlines()
        blocks.append([int(block[4].split()[2]), int(block[5].split()[2]), int(block[15].split()[2])])
    return blocks

def parseBlock(commands, digit, z)->int:
    vars = {"w": 0, "x" : 0, "y" : 0, "z" : z}
    for c in commands:
        if c[0] == "inp":
            vars[c[1]] = int(digit)
        else:
            func = instructions.get(c[0], "invalid")
            if c[2].lstrip('-').isdigit():
                vars[c[1]] = func(vars[c[1]], int(c[2]))
            else:
                vars[c[1]] = func(vars[c[1]], vars[c[2]])
    return vars["z"]

def calc_digit(command_blocks, depth, z):
    for digit in range(1, 10):
        if depth in block_dic:
            n_z = block_dic[depth](0, digit)
        else:
            n_z = parseBlock(command_blocks[depth], digit, z)
        if depth == 13:
            if n_z == 0:
                return True, str(digit)
            else:
                return False, 0
        r, num = calc_digit(command_blocks, depth+1, n_z)
        if r:
            return r, str(digit) + num
    return False, 0

def getPossibleInput(block, zout):
    # find all possible zin, w pairs
    pairs = []
    if block[0] == 26:
        for w in range(1, 10):
            pairs.append((26 * zout + w - block[1], w))
    else:
        for w in range(1, 10):
            num_to_divide = zout - (w + block[2])
            if num_to_divide % 26 != 0:
                # input only interger ther for sort out fractured
                continue
            pairs.append((num_to_divide / 26, w))

    return pairs

# solve bottom-up, expecting zout = 0 at the end and zin = 0 at the start
def solve(blocks, target, solutions, current):
    if len(blocks) == 0:
        if target == 0:
             solutions.append(current)
        return solutions
    for zin, w in getPossibleInput(blocks[0], target):
        solve(blocks[1:], zin, solutions, str(w) + current)
    return solutions

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

command_blocks = readValues(file_path)
command_blocks.reverse()

solutions = solve(command_blocks, 0, [], "")
print("solve count", len(solutions))
print("max", max(solutions))
print("min", min(solutions))

#print("commands", command_blocks)
