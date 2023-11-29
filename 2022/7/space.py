#!/usr/bin/python
import os
from collections import deque, defaultdict

def buildTree(lines):
    line_list = deque(lines)
    fs    = defaultdict(list)
    crr_path  = ()

    while line_list:
        _, command, *args = line_list.popleft().split()

        if command == 'ls':
            while line_list and not line_list[0].startswith('$'):
                size = line_list.popleft().split()[0]
                if size != 'dir':
                    fs[crr_path].append(int(size))
        else:
            if args[0] == '..':
                crr_path = crr_path[:-1]
            else:
                new_path = crr_path + (args[0],)
                fs[crr_path].append(new_path)
                crr_path = new_path

    return fs

def directory_size(directory):
    size = 0

    for subdir_or_size in fs[directory]:
        if isinstance(subdir_or_size, int):
            size += subdir_or_size
        else:
            size += directory_size(subdir_or_size)

    return size


path = os.path.dirname(__file__)
file_path = os.path.join(path, "input.txt")

with open(file_path) as f:
    lines = f.readlines()

fs = buildTree(lines)

used = directory_size(('/',))
free = 70000000 - used
need = 30000000 - free

small_dir_total  = 0
min_size_to_free = used

for directory in fs:
    dir_size = directory_size(directory)

    if dir_size <= 100000:
        small_dir_total += dir_size
    if dir_size >= need and dir_size < min_size_to_free:
        min_size_to_free = dir_size

print(small_dir_total) #1845346
print(min_size_to_free)#3636703