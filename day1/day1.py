def part1():
    lines = None
    with open("input.txt", "r") as f:
        lines = f.readlines()

    cal = 0
    res = 0
    for line in lines:
        if line.strip():
            cal += int(line)
        else:
            res = max(res, cal)
            cal = 0
    return max(res, cal)


def part2():
    lines = None
    with open("input.txt", "r") as f:
        lines = f.readlines()

    cals = []
    cal = 0
    for line in lines:
        if line.strip():
            cal += int(line)
        else:
            cals.append(cal)
            cal = 0

    scals = [0 for _ in range(max(cals) + 1)]
    for cal in cals:
        scals[cal] += 1

    res = 0
    limit = 3
    for i in range(len(scals) - 1, -1, -1):
        count = scals[i]
        while count > 0 and limit > 0:
            res += i
            limit -= 1
            count -= 1

        if limit == 0:
            break

    return res


# main functions
if __name__ == "__main__":
    print(part1())
    print(part2())