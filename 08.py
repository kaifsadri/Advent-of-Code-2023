from collections import deque
from math import lcm

IN = list(line.strip() for line in open("08.txt").readlines())
D = deque(IN[0])

M = dict()
for line in IN[2:]:
    k, v = line.split(" = ")
    l, r = v[1:-1].split(", ")
    M[k] = (l, r)

P1 = 0
L = "AAA"
while L != "ZZZ":
    P1 += 1
    step = D.popleft()
    if step == "L":
        L = M[L][0]
    elif step == "R":
        L = M[L][1]
    else:
        print("ERROR!", step)
    D.append(step)

print(f"Part 1: {P1}")


def examine(node):
    global M
    D = deque(IN[0])
    L = node
    res1 = 0
    while L[-1] != "Z":
        res1 += 1
        step = D.popleft()
        if step == "L":
            L = M[L][0]
        elif step == "R":
            L = M[L][1]
        else:
            print("ERROR!", step)
        D.append(step)
    res2 = 1
    step = D.popleft()
    if step == "L":
        L = M[L][0]
    elif step == "R":
        L = M[L][1]
    else:
        print("ERROR!", step)
    D.append(step)
    while L[-1] != "Z":
        res2 += 1
        step = D.popleft()
        if step == "L":
            L = M[L][0]
        elif step == "R":
            L = M[L][1]
        else:
            print("ERROR!", step)
        D.append(step)
    return res1, res2


P2 = list()
for p in M:
    if p[-1] != "A":
        continue
    P2.append(examine(p)[1])
# study of the examine() output showed that the number of steps to the first "Z"
# and cycles to repeat back to the "Z" where the same. This simplifies the output!
print(f"Part 2: {lcm(*P2)}")
