L = list(line.strip() for line in open("05.txt").readlines() if line != "\n")

R = [[int(x) for x in L[0][7:].split()]]

temp = list()
for line in L[1:]:
    if ":" not in line:
        temp.append(tuple(int(x) for x in line.split(" ")))
    else:
        if temp:
            R.append(temp.copy())
            temp.clear()
R.append(temp.copy())

# P1 - find the smallest location for any of the seeds


def grab(number, mapping):
    result = number
    for item in mapping:
        destination, source, length = item
        if source <= number <= source + length:
            return destination + number - source
    return result


P1 = list()
for seed in R[0]:  # for each seed
    n = seed
    for m, mapping in enumerate(R[1:]):
        n = grab(n, mapping)
    P1.append(n)
print(f"Part 1: {min(P1)}")


# Part 2: we need to re-process the data in R so that there is a full mapping between the initial seed and the final location. This mapping is basically a range and the offset that applies to the range.
