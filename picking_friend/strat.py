#! /usr/bin/env python3

fdir = input("enter friend direction(n/s/e/w): ")
fdist = int(input("enter friend dist: "))

dir_mapping = {
    "n": [0, 1],
    "s": [0, -1],
    "e": [1, 0],
    "w": [-1, 0]
}


fpos = [dir*fdist for dir in dir_mapping[fdir]]

mindist = 20

mdir = "e"
mdist = 0

x = 0
y = 0

mpos = [x, y]

rad = 1

y = rad

totaldistcovered = 0.0

while rad<20:
    distcovered = 0

    for i in range(rad):
        if mpos == fpos:
            print("found:", mpos)
            break
        x = i
        y = rad - i

    for i in range(mpos[0], 0, -1):
        if mpos == fpos:
            print("found:", mpos)
            break
        x = mpos[0]
        y = x - rad
    for i in range(mpos[0], -1, -1):
        if mpos == fpos:
            print("found:", mpos)
            break
        x = mpos[0]
        y = -x - rad
    for i in range(-1, 1):
        if mpos == fpos:
            print("found:", mpos)
            break
        x = mpos[0]
        y = x + rad

    rad += 1


fvis = False

covdist = 0
# print("friend:", fdir, fdist)
# print("my:", mdir, mdist)


def movedir(fdir, fdist, mdir, mdist, mindist, fvis):
    vis = fvis
    while mdist < mindist:
        if fdir == mdir and fdist == mdist:
            return mdist, True
        mdist += 1

    if mdist == mindist and mdir == fdir:
        vis = True

    while vis:
        if mdist == fdist:
            return mdist, True
        mdist += 1

    return mdist, False


def back2origin(dir):
    return dir, 0


de, found = movedir(fdir, fdist, mdir, mdist, mindist, fvis)
covdist += de

print("distance covered:", covdist, "direction:", mdir, "found:", found)

if not found:
    covdist += de
    mdir, mdist = back2origin("n")
    dn, found = movedir(fdir, fdist, mdir, mdist, mindist, fvis)
    covdist += dn

    print("distance covered:", covdist, "direction:", mdir, "found:", found)

if not found:
    covdist += dn
    mdir, mdist = back2origin("s")
    ds, found = movedir(fdir, fdist, mdir, mdist, mindist, fvis)
    covdist += ds

    print("distance covered:", covdist, "direction:", mdir, "found:", found)

if not found:
    covdist += ds
    mdir, mdist = back2origin("w")
    dw, found = movedir(fdir, fdist, mdir, mdist, mindist, fvis)
    covdist += dw

    print("distance covered:", covdist, "direction:", mdir, "found:", found)
