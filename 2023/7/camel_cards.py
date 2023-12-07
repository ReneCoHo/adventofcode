#!/usr/bin/python
import os

path = os.path.dirname(__file__)
file_path = os.path.join(path, "small_input.txt")
file_path = os.path.join(path, "input.txt")

order1 = {'2' : '11',
         '3' : '12',
         '4' : '13',
         '5' : '14',
         '6' : '15',
         '7' : '16',
         '8' : '17',
         '9' : '18',
         'T' : '19',
         'J' : '20',
         'Q' : '21',
         'K' : '22',
         'A' : '23'
         }

order2 = {
         'J' : '11',
         '2' : '12',
         '3' : '13',
         '4' : '14',
         '5' : '15',
         '6' : '16',
         '7' : '17',
         '8' : '18',
         '9' : '19',
         'T' : '20',
         'Q' : '21',
         'K' : '22',
         'A' : '23'
         }

def getSortedHands(input, order, joker):
    sortedHands = {x:set() for x in range(1,8)}

    for line in input:
        hand = line.split(' ')
        value = int(''.join([order[x] for x in hand[0] if x in order]))
        times = {}
        if joker:
            timesJ = hand[0].count(joker)
        else:
            timesJ = 0
        for c in hand[0]:
            if joker:
                if c != joker:
                    times[c] = hand[0].count(c)
            else:
                times[c] = hand[0].count(c)
        if times:
            maxKey = max(times, key=times.get)
            timesMax = int(times[maxKey])
        else:
            timesMax = 0

        if timesMax + timesJ == 5:
            type = 7
        elif timesMax + timesJ == 4:
            type = 6
        else:
            times.pop(maxKey)
            timesMax2 = int(times[max(times, key=times.get)])
            if timesMax + timesJ == 3  and timesMax2 == 2:
                type = 5
            elif timesMax + timesJ == 3:
                type = 4
            elif timesMax == 2 and timesMax2 + timesJ == 2:
                type = 3
            elif timesMax + timesJ == 2:
                type = 2
            else:
                type = 1

        sortedHands[type].add((value, int(hand[1])))
    return sortedHands

def calcResult(sortedHands):
    res = 0
    i = 1
    for hands in sortedHands.values():
        shands = sorted(hands)
        for handBid in shands:
            res += handBid[1]*i
            i += 1
    return res

with open(file_path) as f:
    input = f.read().splitlines()

sortedHands = getSortedHands(input, order1, None)
result = calcResult(sortedHands)
print("1:", result)

sortedHands = getSortedHands(input, order2, 'J')
result = calcResult(sortedHands)
print("2:", result)