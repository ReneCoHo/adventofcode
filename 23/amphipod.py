#!/usr/bin/env python3
import math

A, B, C, D = range(4)
room_pos = (2, 4, 6, 8)
move_floor_pos = (0, 1, 3, 5, 7, 9, 10)

end_pods = {(2,1):A, (2,2):A,\
            (4,1):B, (4,2):B,\
            (6,1):C, (6,2):C,\
            (8,1):D, (8,2):D }

def moveCost(p0, p1, t):
    return (abs(p0[0]-p1[0]) + abs(p0[1]-p1[1]))*10**t

def end(floor, rooms)->bool:
    for amp in floor:
        if not amp is None:
            return False

    return rooms == end_rooms

def insert(t, i, insert_val):
    return t[:i] + (insert_val,) + t[i + 1 :]

def hasPath(to, pos, floor)->bool:
    for i in range(min(pos,to), max(pos,to)+1):
        if i in room_pos:
            continue
        if floor[i] is not None:
            return False
    return True

def hasPathToRoom(to, pos, floor)->bool:
    for p in range(min(to, pos)+1,max(to, pos)):
        if p in room_pos:
            continue
        if floor[p] is not None:
            return False
    return True    

def move(floor, rooms, depth, cost_map)->int:
    if end(floor, rooms):
        return 0

    min_costs = math.inf
    #from room to floor
    for r_i, room in enumerate(rooms):
        if room and not all(amp == r_i for amp in room):
            amp = room[-1]

            for f_pos in move_floor_pos:
                if not hasPath(room_pos[r_i], f_pos, floor):
                    continue
                n_floor = insert(floor, f_pos, amp)
                n_rooms = insert(rooms, r_i, room[:-1])
                if (n_floor, n_rooms) in cost_map:
                    sub_cost = cost_map[(n_floor, n_rooms)]
                else:
                    sub_cost = move(n_floor, n_rooms, depth + 1, cost_map)
                    cost_map[(n_floor, n_rooms)] = sub_cost

                if sub_cost == math.inf:
                    continue
                move_cost = (room_size - len(room) + 1 + abs(room_pos[r_i] - f_pos))* (10 ** amp)
                min_costs = min(min_costs, move_cost + sub_cost)
    #from floor to room
    for i, amp in enumerate(floor):
        if amp is None:
            continue
        target_pos = room_pos[amp]
        if not hasPathToRoom(i, target_pos, floor):
            continue
        if any(u != amp for u in rooms[amp]):
            continue
        n_rooms = insert(rooms, amp, (rooms[amp] + (amp,)))
        n_floor = insert(floor, i, None)

        if ((n_floor, n_rooms)) in cost_map:
            sub_cost = cost_map[(n_floor, n_rooms)]
        else:
            sub_cost = move(n_floor, n_rooms, depth + 1, cost_map)
            cost_map[(n_floor, n_rooms)] = sub_cost

        if sub_cost == math.inf:
            continue

        move_cost = (room_size - len(rooms[amp]) + abs(target_pos - i)) * (10 ** amp)
        min_costs = min(min_costs, move_cost + sub_cost)

    return min_costs

floor: tuple = (None,) * 11
rooms = ((D,C), (D,A), (B,B), (A,C))
end_rooms = ((A,A), (B,B), (C,C), (D,D))
room_size = len(end_rooms[0])

cost_map = {}
#total = move(floor, rooms, 0, cost_map)
#print("cost 1", total)
#exit(0)

end_rooms = ((A,A,A,A), (B,B,B,B), (C,C,C,C), (D,D,D,D))
room_size = len(end_rooms[0])
rooms = (
    (rooms[0][0], D, D, rooms[0][1]),
    (rooms[1][0], B, C, rooms[1][1]),
    (rooms[2][0], A, B, rooms[2][1]),
    (rooms[3][0], C, A, rooms[3][1]),
)

total = move(floor, rooms, 0, cost_map)
print("cost 2", total)