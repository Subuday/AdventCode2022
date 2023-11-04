from collections import deque

def part1():
    stack1 = deque(['F', 'C', 'J', 'P', 'H', 'T', 'W'])
    stack2 = deque(['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'])
    stack3 = deque(['H', 'P', 'T', 'R'])
    stack4 = deque(['Z', 'S', 'N', 'P', 'H', 'T'])
    stack5 = deque(['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'])
    stack6 = deque(['P', 'M', 'G', 'F', 'W', 'D', 'Z'])
    stack7 = deque(['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'])
    stack8 = deque(['N', 'D', 'S'])
    stack9 = deque(['D', 'Z', 'S', 'F', 'M'])

    stacks = [None, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    commands = None
    with open("input.txt", "r") as f:
        def parse(line):
            arr = line.strip().split(' ')
            return [int(arr[1]), int(arr[3]), int(arr[5])]

        commands = list(map(lambda s: parse(s), f.readlines()))

    for command in commands:
        count = command[0]
        fr = command[1]
        to = command[2]

        while count > 0:
            stacks[to].append(stacks[fr].pop())
            count -= 1

    res = ""
    for stack in stacks[1:]:
        res += stack[-1]
    return res

def part2():
    stack1 = deque(['F', 'C', 'J', 'P', 'H', 'T', 'W'])
    stack2 = deque(['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'])
    stack3 = deque(['H', 'P', 'T', 'R'])
    stack4 = deque(['Z', 'S', 'N', 'P', 'H', 'T'])
    stack5 = deque(['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'])
    stack6 = deque(['P', 'M', 'G', 'F', 'W', 'D', 'Z'])
    stack7 = deque(['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'])
    stack8 = deque(['N', 'D', 'S'])
    stack9 = deque(['D', 'Z', 'S', 'F', 'M'])

    stacks = [None, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    commands = None
    with open("input.txt", "r") as f:
        def parse(line):
            arr = line.strip().split(' ')
            return [int(arr[1]), int(arr[3]), int(arr[5])]

        commands = list(map(lambda s: parse(s), f.readlines()))

    for command in commands:
        count = command[0]
        fr = command[1]
        to = command[2]

        crates = []
        while count > 0:
            crates.append(stacks[fr].pop())
            count -= 1
        while len(crates) > 0:
            stacks[to].append(crates.pop())

    res = ""
    for stack in stacks[1:]:
        res += stack[-1]
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())