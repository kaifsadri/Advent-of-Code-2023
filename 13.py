L = list(line.strip() for line in open("13.txt").readlines()) + [""]  # Algo needs and empty line in the end.
P1 = 0
P2 = 0
block = dict()
row = 0
for line in L:
    if line == "":
        for border in range(col):  # col is the number of columns in the image
            flag = True
            delta = 0
            b = border + 0.5
            mirrored = dict(((coord[0], 2 * b - coord[1]), block[coord]) for coord in block)
            for item in set(mirrored) & set(block):
                if mirrored[item] != block[item]:
                    flag = False  # for part 1 we reject it if there is no reflection
                    delta += 1  # for part 2 we seek a condition with precisely two differences
            if flag:
                P1 += border + 1
            if delta == 2:  # accounting for double-counting
                P2 += border + 1
        for border in range(row - 1):  # row - 1 is the number of rows in the image
            flag = True
            delta = 0
            b = border + 0.5
            mirrored = dict()
            for coord in block:
                mirrored[(2 * b - coord[0], coord[1])] = block[coord]
            for item in set(mirrored) & set(block):
                if mirrored[item] != block[item]:
                    flag = False
                    delta += 1
            if flag:
                P1 += 100 * (border + 1)
            if delta == 2:
                P2 += 100 * (border + 1)
        block.clear()
        row = 0
    else:
        for col, c in enumerate(line):
            block[(row, col)] = c
        row += 1
print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
