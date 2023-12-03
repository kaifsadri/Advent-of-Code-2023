from collections import defaultdict

L = list(list(line.strip()) for line in open("03.txt").readlines())


def adj(row, col):
    s = set()
    for r in range(-1, 2):
        for c in range(-1, 2):
            s.add((row + r, col + c))
    return s


nums = set("0123456789")
numsdot = set(".0123456789")

# Part 1
n = list()  # numbes we find going through
d = 0  # flag to signal there is a symbol around
P1 = 0
for row, line in enumerate(L):
    for col, char in enumerate(line):
        if char not in nums:  # if a number ends or we see something uninteresting
            if len(n) > 0:
                if d != 0:
                    P1 += int("".join(n))
                    d = 0
                n.clear()
        else:  # here we hit a number
            n.append(char)
            for coord in adj(row, col):
                try:
                    if L[coord[0]][coord[1]] not in numsdot:
                        d = 1
                except IndexError:
                    pass
print(f"Part 1: {P1}")

# Part 2
n = list()  # numbers we find going through
gears = set()  # this now holds the coordinates of all *s next to a number
S = defaultdict(list)
for row, line in enumerate(L):
    for col, char in enumerate(line):
        if char not in nums:  # if a number ends or we see something uninteresting
            if len(n) > 0:
                for gear in gears:
                    S[gear].append(int("".join(n)))
                gears.clear()
                n.clear()
        else:  # here we hit a number
            n.append(char)
            for coord in adj(row, col):
                try:
                    if L[coord[0]][coord[1]] == "*":  # if we find a gear
                        gears.add(coord)
                except IndexError:
                    pass

print(f"Part 2: {sum(p[0]*p[1] for p in S.values() if len(p) ==2)}")
