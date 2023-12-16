import sys
from collections import defaultdict, OrderedDict


def HASH(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


L = open(sys.argv[1]).readline().strip().split(",")
print(f"Part 1: {sum(map(HASH, L))}")

P2 = 0
D = defaultdict(OrderedDict)
for it in L:
    if "-" in it:
        lb = it[:-1]
        bx = HASH(lb)
        D[bx].pop(lb, None)
    elif "=" in it:
        lb, f = it.split("=")
        f = int(f)
        bx = HASH(lb)
        D[bx][lb] = f
for box in D:
    for slot, lb in enumerate(D[box]):
        P2 += (box + 1) * (slot + 1) * D[box][lb]
print(f"Part 2: {P2}")
