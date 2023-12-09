L = list(list(map(lambda x: int(x), line.strip().split(" "))) for line in open("09.txt").readlines())
P1 = 0
for line in L:
    l = line.copy()
    p = l[-1]
    while l != [0] * len(l):
        l = list(l[t + 1] - l[t] for t in range(len(l) - 1))
        p += l[-1]
    P1 += p
print(f"Part 1: {P1}")

# Part 2 reverse history is the same as forward hitory for reversed sequences
P2 = 0
for line in L:
    l = line[-1::-1]
    p = l[-1]
    while l != [0] * len(l):
        l = list(l[t + 1] - l[t] for t in range(len(l) - 1))
        p += l[-1]
    P2 += p
print(f"Part 2: {P2}")
