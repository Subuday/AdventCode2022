
def part1():
    pairs = None
    with open("input.txt", "r") as f:
        def parse(line):
            line = line.strip()
            line = list(map(lambda s: list(map(lambda string: int(string), s.split("-"))), line.split(",")))
            return line
        pairs = list(map(lambda s: parse(s), f.readlines()))

    res = 0
    for pair in pairs:
        asgn1 = pair[0]
        asgn2 = pair[1]

        if ((asgn1[0] <= asgn2[0] and asgn1[1] >= asgn2[1]) or
            (asgn2[0] <= asgn1[0] and asgn2[1] >= asgn1[1])):
            res += 1

    return res

def part2():
    pairs = None
    with open("input.txt", "r") as f:
        def parse(line):
            line = line.strip()
            line = list(map(lambda s: list(map(lambda string: int(string), s.split("-"))), line.split(",")))
            return line
        pairs = list(map(lambda s: parse(s), f.readlines()))

    res = 0
    for pair in pairs:
        asgn1 = pair[0]
        asgn2 = pair[1]

        if ((asgn1[0] <= asgn2[1] and asgn1[1] >= asgn2[0]) or
            (asgn2[0] <= asgn1[1] and asgn2[1] >= asgn1[0])):
            res += 1

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())