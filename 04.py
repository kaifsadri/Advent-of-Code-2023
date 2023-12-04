L = list(line.strip() for line in open("04.txt").readlines())
P1 = 0
P2 = [1] * len(L)
for card, line in enumerate(L):
    t = line.split(":")
    winners = set(map(lambda x: int(x), t[1].split(" | ")[0].split()))
    numbers = list(map(lambda x: int(x), t[1].split(" | ")[1].split()))
    n = sum(1 for k in numbers if k in winners)
    if n > 0:  # here both parts happen
        P1 += 2 ** (n - 1)
        for c in range(n):
            P2[card + c + 1] += P2[card]
print(f"Part 1: {P1}")
print(f"Part 2: {sum(P2)}")
