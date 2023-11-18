import functools


def parse(line):
    stack = [[]]
    i = 0
    while i < len(line):
        c = line[i]
        if c == '[':
            stack.append([])
        elif c == ']':
            array = stack.pop()
            stack[-1].append(array)
        elif c == ',':
            pass
        else:
            num = ""
            num += c
            while line[i + 1] != ',' and line[i + 1] != ']':
                num += line[i + 1]
                i += 1
            stack[-1].append(int(num))
        i += 1

    return stack[0][0]


def compare(l, r):
    i = 0
    while i < len(l) and i < len(r):
        if type(l[i]) is list or type(r[i]) is list:
            left = l[i]
            if type(l[i]) is int:
                left = [left]

            right = r[i]
            if type(r[i]) is int:
                right = [right]

            cmp = compare(left, right)
            if cmp == 1 or cmp == -1:
                return cmp
        elif l[i] < r[i]:
            return 1
        elif l[i] > r[i]:
            return -1

        i += 1

    if len(l) < len(r):
        return 1
    elif len(l) > len(r):
        return -1
    else:
        return 0

def part1():
    pairs = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        i = 0
        while i < len(lines):
            pairs.append((parse(lines[i]), parse(lines[i + 1])))
            i += 3

    res = 0
    for i in range(len(pairs)):
        if compare(pairs[i][0], pairs[i][1]) == 1:
            res += i + 1

    return res

def part2():
    signals = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        i = 0
        while i < len(lines):
            signals.append(parse(lines[i]))
            signals.append(parse(lines[i + 1]))
            i += 3

    signals.append([[2]])
    signals.append([[6]])

    signals.sort(key=functools.cmp_to_key(compare), reverse=True)

    return (signals.index([[2]]) + 1) * (signals.index([[6]]) + 1)

if __name__ == "__main__":
    print(part1())
    print(part2())