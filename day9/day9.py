import math


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def dist_vec(a, b):
    return a[0] - b[0], a[1] - b[1]

def simulate(knots):
    cmds = None
    with open("input.txt", "r") as f:
        def parse(line):
            line = line.strip()
            d, s = line.split(' ')
            return d, int(s)

        cmds = list(map(lambda s: parse(s), f.readlines()))

    visited = set()
    i = 0
    visited.add((0, 0))
    while True:
        if i >= len(cmds):
            break

        d, s = cmds[i]

        while s > 0:
            H = knots[len(knots) - 1]
            if d == 'U':
                H = (H[0] + 1, H[1])
            elif d == 'D':
                H = (H[0] - 1, H[1])
            elif d == 'R':
                H = (H[0], H[1] + 1)
            else:
                H = (H[0], H[1] - 1)
            knots[len(knots) - 1] = H

            for j in range(len(knots) - 2, -1, -1):
                H = knots[j + 1]
                T = knots[j]
                if dist(H, T) >= 2:
                    d_v_x, d_v_y = dist_vec(H, T)

                    if d_v_x > 0 and d_v_y > 0:
                        T = (T[0] + 1, T[1] + 1)
                    elif d_v_x > 0 and d_v_y < 0:
                        T = (T[0] + 1, T[1] - 1)
                    elif d_v_x < 0 and d_v_y > 0:
                        T = (T[0] - 1, T[1] + 1)
                    elif d_v_x < 0 and d_v_y < 0:
                        T = (T[0] - 1, T[1] - 1)
                    elif d_v_x == 0 and d_v_y > 0:
                        T = (T[0], T[1] + 1)
                    elif d_v_x == 0 and d_v_y < 0:
                        T = (T[0], T[1] - 1)
                    elif d_v_x > 0 and d_v_y == 0:
                        T = (T[0] + 1, T[1])
                    else:
                        T = (T[0] - 1, T[1])
                    knots[j] = T

                    if j == 0:
                        visited.add(T)
            s -= 1

        i += 1

    return len(visited)

def part1():
    return simulate([(0, 0) for _ in range(2)])




def part2():
    return simulate([(0, 0) for _ in range(10)])


if __name__ == "__main__":
    print(part1())
    print(part2())