#!/usr/bin/python
global d_count

def roll(dice):
    return (dice % 100) + 1

def move(pos, dice):
    dice = roll(dice)
    pos = (pos + dice - 1)%10 + 1

    dice = roll(dice)
    pos = (pos + dice - 1)%10 + 1

    dice = roll(dice)
    pos = (pos + dice - 1)%10 + 1
    return pos, dice

def turn(P):
    pts = [0, 0]
    count = 0
    dice = 0

    while True:
        #print("turn:", i)
        P[0], dice = move(P[0], dice)
        count += 3
        pts[0] += P[0]
        if pts[0] >= 1000:
            return pts[1]*count

        P[1], dice = move(P[1], dice)
        count += 3
        pts[1] += P[1]
        if pts[1] >= 1000:
            return pts[0]*count

        #print("pos:", P[0], P[1])
        #print("pts:", pts[0], pts[1])
        #print("dice", dice)

P = [3, 5]
print("res:", turn(P))
