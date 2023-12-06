#!/usr/bin/python
import math

def calcWinF(times, distances):
    win_prod = 1
    for t, d in zip(times, distances):
        if t%2 == 0:
            win_prod *= 1 + 2*math.floor(math.sqrt( (t/2)**2 - d))
        else:
            win_prod *= 2*math.floor(0.5 + math.sqrt( (t/2)**2 - d))
    return win_prod

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

#print("1:", calcWin(times, distances))# correct ans 1413720
print("1:", calcWinF(times, distances))

#times = [71530]
#distances = [940200]

times = [45988373]
distances = [295173412781210]

print("2:", calcWinF(times, distances)) # correct ans 30565288