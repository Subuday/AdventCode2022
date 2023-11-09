
def part1():
    cmds = None
    with open("input.txt", "r") as f:
        def parse(line):
            return line.strip().split(' ')

        cmds = list(map(lambda s: parse(s), f.readlines()))

    res = 0
    cycles = 0
    sum = 1
    pendingValue = None
    while cmds or pendingValue:
        cycles += 1

        if cycles in {20, 60, 100, 140, 180, 220}:
            res += (sum * cycles)

        if pendingValue is None:
            cmd = cmds.pop(0)
            if cmd[0] == "addx":
                pendingValue = int(cmd[1])
        else:
            sum += pendingValue
            pendingValue = None

    return res

def part2():
    with open("input.txt", "r") as f:
        def parse(line):
            return line.strip().split(' ')

        cmds = list(map(lambda s: parse(s), f.readlines()))

    cycles = 0
    sum = 1
    pendingValue = None
    x = 0
    y = 0
    drawing = []
    row = []


    while cmds or pendingValue:
        cycles += 1

        if pendingValue is None:
            cmd = cmds.pop(0)
            if cmd[0] == "addx":
                pendingValue = int(cmd[1])

            if sum - 1 <= x <= sum + 1:
                row.append('#')
            else:
                row.append('.')

            x += 1

            if len(row) == 40:
                drawing.append(row.copy())
                x = 0
                row = []
        elif pendingValue:
            if sum - 1 <= x <= sum + 1:
                row.append('#')
            else:
                row.append('.')

            x += 1

            if len(row) == 40:
                drawing.append(row.copy())
                x = 0
                row = []

            sum += pendingValue
            pendingValue = None


    for row in drawing:
        print(''.join(row))

if __name__ == "__main__":
    print(part1())
    part2()