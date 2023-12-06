#!/usr/bin/python

def calcWin(times, distances):
    win_prod = 1
    for i, t_end in enumerate(times):
        win_count = 0
        for t in range(t_end):
            s = t*(t_end - t)
            if s > distances[i]:
                win_count += 1
        win_prod *= win_count
    return win_prod

times = [45, 98, 83, 73]
distances = [295, 1734, 1278, 1210]

#times = [7, 15, 30]
#distances = [9, 40, 200]

print("1:", calcWin(times, distances))