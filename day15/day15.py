
import re

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1():
    coords = None
    with open("input.txt", "r") as f:
        def parse(l):
            pattern = r'x=(-?\d+),\s*y=(-?\d+)'
            matches = re.findall(pattern, l)
            coordinates = []
            for match in matches:
                x, y = map(int, match)
                coordinates.append((x, y))
            return coordinates

        coords = list(map(lambda s: parse(s), f.readlines()))

    sensors = []
    beacons = []
    for coord in coords:
        sensors.append(coord[0])
        beacons.append(coord[1])

    dists = []
    for i in range(len(sensors)):
        dists.append(dist(sensors[i], beacons[i]))

    Y = 2000000
    intervals = []

    for i, s in enumerate(sensors):
        dx = dists[i] - abs(s[1] - Y)

        if dx <= 0:
            continue

        intervals.append((s[0] - dx, s[0] + dx))

    min_x = min([i[0] for i in intervals])
    max_x = max([i[1] for i in intervals])

    allowed_x = []
    for bx, by in beacons:
        if by == Y:
            allowed_x.append(bx)

    res = 0
    for x in range(min_x, max_x + 1):
        if x in allowed_x:
            continue

        for left, right in intervals:
            if left <= x <= right:
                res += 1
                break

    return res


def part2():
    coords = None
    with open("input.txt", "r") as f:
        def parse(l):
            pattern = r'x=(-?\d+),\s*y=(-?\d+)'
            matches = re.findall(pattern, l)
            coordinates = []
            for match in matches:
                x, y = map(int, match)
                coordinates.append((x, y))
            return coordinates

        coords = list(map(lambda s: parse(s), f.readlines()))

    sensors = []
    beacons = []
    for coord in coords:
        sensors.append(coord[0])
        beacons.append(coord[1])

    dists = []
    for i in range(len(sensors)):
        dists.append(dist(sensors[i], beacons[i]))

    N = len(sensors)

    pos_lines = []
    neg_lines = []
    for i, s in enumerate(sensors):
        d = dists[i]
        neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
        pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

    pos = None
    neg = None

    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            a, b = pos_lines[i], pos_lines[j]

            if abs(a - b) == 2:
                pos = min(a, b) + 1

            a, b = neg_lines[i], neg_lines[j]

            if abs(a - b) == 2:
                neg = min(a, b) + 1

    x, y = (pos + neg) // 2, (neg - pos) // 2
    return x * 4000000 + y

if __name__ == "__main__":
    print(part1())
    print(part2())