
def part1():
    grid = None
    with open("input.txt", "r") as f:
        def parse(line):
            line = line.strip()
            return [int(ch) for ch in line]

        grid = list(map(lambda s: parse(s), f.readlines()))

    ROWS = len(grid)
    COLS = len(grid[0])

    visible = set()
    for r in range(ROWS):
        visible.add((r, 0))
        visible.add((r, COLS - 1))

    for c in range(COLS):
        visible.add((0, c))
        visible.add((ROWS - 1, c))

    def dfs(r, c, dir, height):
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS):
            return True

        if grid[r][c] >= height:
            return False

        if dir == 1:
            return dfs(r - 1, c, dir, height)
        elif dir == -1:
            return dfs(r + 1, c, dir, height)
        elif dir == 2:
            return dfs(r, c + 1, dir, height)
        elif dir == -2:
            return dfs(r, c - 1, dir, height)


    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if (dfs(r + 1, c, -1, grid[r][c]) or
                dfs(r - 1, c, 1, grid[r][c]) or
                dfs(r, c - 1, -2, grid[r][c]) or
                dfs(r, c + 1, 2, grid[r][c])):
                visible.add((r, c))

    return len(visible)


def part2():
    grid = None
    with open("input.txt", "r") as f:
        def parse(line):
            line = line.strip()
            return [int(ch) for ch in line]

        grid = list(map(lambda s: parse(s), f.readlines()))

    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(r, c, dir, height):
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS):
            return 0

        if grid[r][c] >= height:
            return 1

        if dir == 1:
            return 1 + dfs(r - 1, c, dir, height)
        elif dir == -1:
            return 1 + dfs(r + 1, c, dir, height)
        elif dir == 2:
            return 1 + dfs(r, c + 1, dir, height)
        elif dir == -2:
            return 1 + dfs(r, c - 1, dir, height)


    res = 0
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            cur = 1
            cur *= dfs(r + 1, c, -1, grid[r][c])
            cur *= dfs(r - 1, c, 1, grid[r][c])
            cur *= dfs(r, c - 1, -2, grid[r][c])
            cur *= dfs(r, c + 1, 2, grid[r][c])
            res = max(res, cur)
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())