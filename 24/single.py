#!/usr/bin/env python3
import os

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    commands = []
    for line in lines:
        commands.append(line.rstrip().split(' '))
    print("cmd size", len(commands))
    return commands

def parse(commands, input):
    vars = {"w": 0, "x" : 0, "y" : 0, "z" : 0}

    instructions = {
        "add": (lambda a, b: int(a+b)),
        "mul": (lambda a, b: int(a*b)),
        "div": (lambda a, b: int(a/b)),
        "mod": (lambda a, b: int(a%b)),
        "eql": (lambda a, b: int(a==b))
    }
    for c in commands:
        if c[0] == "inp":
            vars[c[1]] = int(input[0])
            input = input[1:]
        else:
            func = instructions.get(c[0], "invalid")
            if c[2].lstrip('-').isdigit():
                vars[c[1]] = func(vars[c[1]], int(c[2]))
            else:
                vars[c[1]] = func(vars[c[1]], vars[c[2]])
    return vars["z"]
    

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")

commands = readValues(file_path)
#print("commands", commands)

print("test:", parse(commands, str(68999999999999)))
print("test:", parse(commands, str(11111111111191)))
#print("test:", parse(commands, str(51939397989999)))
#print("test:", parse(commands, str(11717131211195)))