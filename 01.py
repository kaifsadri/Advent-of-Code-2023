L = list(t.strip() for t in open("01.txt").readlines())

V = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

P1 = 0
P2 = 0
for t in L:
    # first and last findings
    f = dict(
        (digit, (t.find(digit), t.rfind(digit)))
        for digit in "123456789"
        if t.find(digit) > -1 and t.rfind(digit) > -1
    )
    P1 += 10 * V[min(f, key=lambda x: f[x][0])] + V[max(f, key=lambda x: f[x][1])]
    f = dict(
        (digit, (t.find(digit), t.rfind(digit))) for digit in V if t.find(digit) > -1 and t.rfind(digit) > -1
    )
    P2 += 10 * V[min(f, key=lambda x: f[x][0])] + V[max(f, key=lambda x: f[x][1])]

print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
