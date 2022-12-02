#!/usr/bin/python

import os

def isSimple(number):
    return type(number) is int

def magnitude(number):
	if isSimple(number):
		return number
	return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def addToNextLeft(number, simpleNum):
	if isSimple(number):
		return number + simpleNum
	return (addToNextLeft(number[0], simpleNum), number[1])

def addToNextRight(number, simpleNum):
	if isSimple(number):
		return number + simpleNum
	return (number[0], addToNextRight(number[1], simpleNum))

def split(number):
	if isSimple(number):
		if number >= 10:
			a = number // 2
			return (a, number-a), True
		else:
			return number, False
	left, right = number			
	left, sp = split(left)
	if not sp:
		right, sp = split(right)
	return (left, right), sp

def explode(number, depth):
	if isSimple(number):
		return None, number, None, False

	if depth == 4:
		return number[0], 0, number[1], True

	left, right = number
	left_num, left, right_num, changed = explode(left, depth + 1)

	if changed:
		if right_num is None:
			return left_num, (left, right), None, True
		return left_num, (left, addToNextLeft(right, right_num)), None, True

	left_num, right, right_num, changed = explode(right, depth + 1)

	if changed:
		if left_num is None:
			return None, (left, right), right_num, True
		return None, (addToNextRight(left, left_num), right), right_num, True

	return None, number, None, False	

def reduce(number):
	changed = True
	while changed:
		_, number, _, changed = explode(number, 0)
		if changed:
			continue
		number, changed = split(number)
	return number

def add(a, b):
	return reduce((a, b))

def readValues(file_path):
    print("read file:", file_path)
    with open(file_path) as f:
        lines = f.readlines()

    numbers=[]
    for line in lines:
        line = line.replace('[', '(')
        line = line.replace(']', ')')
        tub = tuple(eval(line))
        numbers.append(tub)
        print(tub)
    return numbers

def maxAddMag(numbers):
    max_mag = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            res = magnitude(add(numbers[j], numbers[i]))
            max_mag = max(res, max_mag)
    return max_mag
        

path = os.path.dirname(__file__)
#file_path = os.path.join(path, "test.txt")
file_path = os.path.join(path, "input.txt")
numbers = readValues(file_path)

res = numbers[0]
for i in range(1, len(numbers)):
    res = add(res, numbers[i])

print("mag sum", magnitude(res))

print("max mag", maxAddMag(numbers))

