#!/usr/bin/env python
file_path = "D:\\develop\\personal\\AoC\\2025\\2\\input.txt" # 23560874270, 44143124633
#file_path = "D:\\develop\\personal\\AoC\\2025\\2\\test.txt" # 1227775554
#file_path = "D:\\develop\\personal\\AoC\\2025\\2\\test2.txt" # 4174379265

def read(file_path):
    with open(file_path, "r") as file:
        lines = file.readline()
    ranges_text=lines.split(',')
    ranges=[]
    for rt in ranges_text:
        limit_txt = rt.split('-')
        ranges.append([int(limit_txt[0]), int(limit_txt[1])])
    return ranges

def check_double_ids(data)->int:
    invalid_ids=[]
    for r in data:
        for d in range(r[0], r[1]+1) :
            dtxt = str(d)
            size = len(dtxt)
            if size%2 == 0:
                hs = int(size/2)
                if dtxt[hs:]==dtxt[:hs]:
                    invalid_ids.append(d)
    return invalid_ids

def check_repeat_ids(data)->int:
    invalid_ids=[]
    for r in data:
        for d in range(r[0], r[1]+1) :
            dtxt = str(d)
            size = len(dtxt)
            for part in range(1, 1 + int(size/2)):
                if not size%part == 0:
                    continue
                times = int(size/part)
                equal=True
                for t in range(1, times):
                    pos = t*part
                    if not dtxt[:part]==dtxt[pos:pos+part]:
                        equal=False
                        break
                if equal:
                    invalid_ids.append(d)
                    break
    return invalid_ids

data = read(file_path)
#double_ids = check_double_ids(data)
#print("double id sum:", sum(double_ids))

repeat_ids = check_repeat_ids(data)
print("repeat id sum:", sum(repeat_ids))