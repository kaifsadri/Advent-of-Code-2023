L = list(list(line.strip()) for line in open("11.txt").readlines())
G = list()  # where galaxies are
ER = set(range(len(L)))  # empty rows
EC = set(range(len(L[0])))  # empty columns

for row, r in enumerate(L):
    for col, c in enumerate(r):
        if c == "#":
            G.append([row, col])
            ER.discard(row)  # this row aint empty
            EC.discard(col)  # this col aint empty

ER = sorted(ER, reverse=True)  # must start from the end for expansion
EC = sorted(EC, reverse=True)  # must start from the end for expansion

# Part 1:
for r in ER:
    for g in G:
        if g[0] > r:
            g[0] += 1

for c in EC:
    for g in G:
        if g[1] > c:
            g[1] += 1

P1 = 0
for g1 in range(len(G)):
    for g2 in range(g1, len(G)):
        P1 += abs(G[g1][0] - G[g2][0]) + abs(G[g1][1] - G[g2][1])

print(f"Part 1: {P1}")

# Part 2:
G.clear()
for row, r in enumerate(L):
    for col, c in enumerate(r):
        if c == "#":
            G.append([row, col])

for r in ER:
    for g in G:
        if g[0] > r:
            g[0] += 999_999  # this replaces one empty with 1 million

for c in EC:
    for g in G:
        if g[1] > c:
            g[1] += 999_999  # this replaces one empty with 1 million

P2 = 0
for g1 in range(len(G)):
    for g2 in range(g1, len(G)):
        P2 += abs(G[g1][0] - G[g2][0]) + abs(G[g1][1] - G[g2][1])

print(f"Part 2: {P2}")
