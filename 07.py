L = list(line.strip().split() for line in open("07.txt").readlines())


def rate1(hand: str) -> int:
    # her we can construct a unique rating based on the two metrics given in the puzzle
    # the hands themselves are treated as 5-digit hex numbers, 20 bits.
    # the category is added as a high bit, say 20 + cat, so bit 37 for 5 of a kind
    handnum = int(hand.translate(str.maketrans("AKQJT", "EDCBA")), base=16)
    # turns a hand into a hex number, mapping
    # AKQJT to EDCBA
    catnum = 1 << (20 + sum(map(hand.count, hand)))
    # the number representing the
    # category (e.g. 4 of a kind)
    # of the hand
    # 5 of a kind = 25
    # 4 of a kind = 17
    # ...
    # high card: 5
    return handnum + catnum


B1 = dict()  # list of hands and their bids
for l in L:
    B1[rate1(l[0])] = int(l[1])
R = sorted(B1)  # sorted by ranks, this puts the lowest rank on top, as it should.
P1 = 0
for k, hand in enumerate(R):
    P1 += (k + 1) * B1[hand]
print(f"Part 1: {P1}")


# Part 2 just changes the definitions for the above function


def rate2(hand: str) -> int:
    # Same as rate 1, but here J represents 0
    # and catnum represents maximum of what's possible while replacing J with different numbers
    handnum = int(hand.translate(str.maketrans("AKQJT", "EDC0A")), base=16)
    if "J" not in hand:
        cat = sum(map(hand.count, hand))
    else:
        r = list()
        for c in hand:
            h = hand.replace("J", c)
            r.append(sum(map(h.count, h)))
        cat = max(r)
    catnum = 1 << (20 + cat)
    return handnum + catnum


B2 = dict()  # list of hands and their bids
for l in L:
    B2[rate2(l[0])] = int(l[1])
R = sorted(B2)  # sorted by ranks, this puts the lowest rank on top, as it should.
P2 = 0
for k, hand in enumerate(R):
    P2 += (k + 1) * B2[hand]
print(f"Part 2: {P2}")
