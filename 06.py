# Puzzle input P1
Time = [62, 73, 75, 65]
Distance = [644, 1023, 1240, 1023]

P1 = 1
for c, t in enumerate(Time):
    lo = Distance[c] // t
    hi = t - Distance[c] // t + 1
    while (t - lo) * lo < Distance[c]:
        lo += 1
    while (t - hi) * hi < Distance[c]:
        hi -= 1
    P1 *= hi - lo + 1
print(f"Part 1: {P1}")

# Puzzle input P2
Time = 62737565
Distance = 644102312401023

lo = Distance // Time
hi = Time - Distance // Time + 1
while (Time - lo) * lo < Distance:
    lo += 1
while (Time - hi) * hi < Distance:
    hi -= 1
print(f"Part 2: {hi-lo+1}")
