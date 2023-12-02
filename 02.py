from math import prod

L = list(line.strip() for line in open("02.txt").readlines())

# part 1
P1 = 0
P2 = 0
Criteria = {"red": 12, "green": 13, "blue": 14}
for line in L:
    D = dict()
    game_id = int(line[line.find(" ") + 1 : line.find(":")])
    game_outcome = line[line.find(":") + 2 :]
    handfuls = list(hand.strip() for hand in game_outcome.split(";"))
    for handful in handfuls:
        items = handful.split(", ")
        for item in items:
            t = item.split(" ")
            D[t[1]] = max(int(t[0]), D.get(t[1], 0))
            if int(t[0]) > Criteria[t[1]]:
                game_id = 0
    P1 += game_id
    P2 += prod(D.values())
print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
