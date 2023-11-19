


def part1():
    scan = set()
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            path = list(map(lambda s: list(map(lambda x: x.strip(), s.split(","))), line.split(" -> ")))
            i = 0
            while i + 1 < len(path):
                x1, y1 = int(path[i][0]), int(path[i][1])
                x2, y2 = int(path[i + 1][0]), int(path[i + 1][1])
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        scan.add((x1, y))
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        scan.add((x, y1))
                i += 1

    start = (500, 0)
    rows = max(scan, key=lambda c: c[1])[1] + 1

    sands = 1
    sand = (start[0], start[1])
    while True:
        if sand[1] == rows:
            break

        if (sand[0], sand[1] + 1) not in scan:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in scan:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in scan:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            scan.add((sand[0], sand[1]))
            sand = (start[0], start[1])
            sands += 1

    return sands - 1




def part2():
    scan = set()
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            path = list(map(lambda s: list(map(lambda x: x.strip(), s.split(","))), line.split(" -> ")))
            i = 0
            while i + 1 < len(path):
                x1, y1 = int(path[i][0]), int(path[i][1])
                x2, y2 = int(path[i + 1][0]), int(path[i + 1][1])
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        scan.add((x1, y))
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        scan.add((x, y1))
                i += 1

    start = (500, 0)
    rows = max(scan, key=lambda c: c[1])[1] + 2

    sands = 1
    sand = (start[0], start[1])
    while True:
        if sand[1] != rows - 1 and (sand[0], sand[1] + 1) not in scan:
            sand = (sand[0], sand[1] + 1)
        elif sand[1] != rows - 1 and (sand[0] - 1, sand[1] + 1) not in scan:
            sand = (sand[0] - 1, sand[1] + 1)
        elif sand[1] != rows - 1 and (sand[0] + 1, sand[1] + 1) not in scan:
            sand = (sand[0] + 1, sand[1] + 1)
        elif sand[0] == start[0] and sand[1] == start[1]:
            break
        else:
            scan.add((sand[0], sand[1]))
            sand = (start[0], start[1])
            sands += 1

    return sands


if __name__ == "__main__":
    print(part1())
    print(part2())