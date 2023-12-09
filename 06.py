from multiprocessing import Pool

# Puzzle input
Time = [62, 73, 75, 65]
Distance = [644, 1023, 1240, 1023]

P1 = 1
for c, t in enumerate(Time):
    p = 0
    # most naiive solution
    # for each race, the min/max of holding the button is 0 and t
    for x in range(0, t + 1):
        if (t - x) * x > Distance[c]:
            p += 1
    P1 *= p
print(f"Part 1: {P1}")

Time = 62737565
Distance = 644102312401023


def race(x):
    if (Time - x) * x > Distance:
        return 1
    else:
        return 0


# somewhat more intelligent solution
# with primitive lower and uppre bounds for possible times
with Pool(processes=4) as pool:
    P2 = pool.map(race, range(Distance // Time, Time - Distance // Time + 1))
print(f"Part 2: {sum(P2)}")
