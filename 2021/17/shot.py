#!/usr/bin/python
import math

def step(p, v):
    p = (p[0] + v[0], p[1] + v[1])
    a = v[0]
    if v[0] > 0:
        a -=1
    return p, (a , v[1]-1)

def isInside(p, area):
    return area[0][0] <= p[0] and  p[0] <= area[0][1] and area[1][0] <= p[1] and  p[1] <= area[1][1] 

def makeSteps(field, target, p, v, n):
    high=[]
    for i in range(n):
        p, v = step(p, v)
        #print(i, p)
        high.append(p[1])
        if not isInside(p, field):
            return []
        if isInside(p, target):
            #print("hit")
            break
    return high

field = [(0,285),(-110, math.inf)]
target = [(230,283),(-107, -57)]
#target = [(20,30), (-10,-5)]

maxh = 0
hit_values=[]
for x in range(15, 300):
    for y in range(-108, 500):
        h = makeSteps(field, target, (0,0), (x, y), 1000)
        if h:
            hit_values.append((x,y))
            if maxh < max(h):
                maxh = max(h)
                print(maxh, x, y)

print(len(hit_values))