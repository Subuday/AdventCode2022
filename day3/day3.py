
def part1():
    rucksacks = None
    with open("input.txt", "r") as f:
        rucksacks = map(lambda s: s.strip(), f.readlines())

    res = 0
    for rucksack in rucksacks:
        if len(rucksack) // 2 == 1:
            raise Exception("Invalid input")

        mid = len(rucksack) // 2
        rucksack1 = set(rucksack[:mid])
        rucksack2 = set(rucksack[mid:])

        for item in rucksack:
            if item in rucksack1 and item in rucksack2:
                if item.isupper():
                    res += ord(item) - ord('A') + 27
                else:
                    res += ord(item) - ord('a') + 1
                break

    return res

def part2():
    groups = None
    with open("input.txt", "r") as f:
        rucksacks = list(map(lambda s: s.strip(), f.readlines()))
        groups = [rucksacks[n:n + 3] for n in range(0, len(rucksacks), 3)]

    res = 0
    for group in groups:
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in group[0] and chr(i) in group[1] and chr(i) in group[2]:
                res += i - ord('a') + 1
                break

        for i in range(ord('A'), ord('Z') + 1):
            if chr(i) in group[0] and chr(i) in group[1] and chr(i) in group[2]:
                res += i - ord('A') + 27
                break

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())