#! /usr/bin/env python3

import math

fdir = input("enter friend direction(n/s/e/w): ")
fdist = int(input("enter friend dist: "))

dir_mapping = {
    "n": [0, 1],
    "s": [0, -1],
    "e": [1, 0],
    "w": [-1, 0]
}

fpos = [dir*fdist for dir in dir_mapping[fdir]]
# print(fpos)

totalDistance = 0

mpos = [0, 0]

rad = 1

mpos[1] = rad
totalDistance += rad

found = False

while not found:

    if not found:
        for i in range(0, rad+1):
            print("coords:", mpos)
            if mpos == fpos:
                print("found:", mpos)
                found = True
                break
            mpos[0] = i
            mpos[1] = rad - i

    if not found:
        for i in range(1, 0, -1):
            print("coords:", mpos)
            if mpos == fpos:
                print("found:", mpos)
                found = True
                break
            mpos[0] = i
            mpos[1] = mpos[0] - rad

    if not found:
        for i in range(0, -1, -1):
            print("coords:", mpos)
            if mpos == fpos:
                print("found:", mpos)
                found = True
                break
            mpos[0] = i
            mpos[1] = -mpos[0] - rad

    if not found:
        for i in range(-1, 1):
            print("coords:", mpos)
            if mpos == fpos:
                print("found:", mpos)
                found = True
                break
            mpos[0] = i
            mpos[1] = mpos[0] + rad

    if not found:
        dist = 4 * rad * math.sqrt(2)
        dist += 1
        totalDistance += dist

    rad += 1


print("total Distance covered:", totalDistance)
