#!/usr/bin/python
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

P = [3, 5]
print("res:", turn(P))


win_map = {}

def recur(player, positions, pts):
    key = str(player) + ' ' + str(positions[0]) + ' ' + str(positions[1]) + ' ' + str(pts[0]) + ' ' + str(pts[1])

    if key in win_map:
        return win_map[key]

    if pts[0] >= 21:
        return [1, 0]
    if pts[1] >= 21:
        return [0, 1]

    wins = [0, 0]

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                next_pos = [positions[0], positions[1]]
                next_pts = [pts[0], pts[1]]
                next_pl = (player+1)%2

                new_pos = (positions[player] + i + j + k - 1) % 10 + 1

                next_pts[player] += new_pos
                next_pos[player] = new_pos
                
                win_res = recur(next_pl, next_pos, next_pts)
                wins[0] += win_res[0]
                wins[1] += win_res[1]		

    win_map[key] = wins
    return wins

print(max(recur(0, [3, 5], [0, 0])))