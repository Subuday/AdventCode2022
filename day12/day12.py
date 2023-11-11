from collections import deque

def bfs(grid, cur_r, cur_c, tar_r, tar_c):
    q = deque([(cur_r, cur_c, 0, 0)])
    visited = set()
    res = float('inf')
    while q:
        r, c, prev, steps = q.popleft()

        if r < 0 or r >= len(grid) or\
           c < 0 or c >= len(grid[r]) or \
           (ord(grid[r][c]) - ord('a')) - prev > 1 or\
           (r, c) in visited:
            continue

        if r == tar_r and c == tar_c:
            res = steps
            break

        visited.add((r, c))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            q.append((r + dr, c + dc, ord(grid[r][c]) - ord('a'), steps + 1))

    return res

def part1():
    grid = None
    with open("input.txt", "r") as f:
        line = list(map(lambda s: s.strip(), f.readlines()))
        grid = [list(w) for w in line]

    cur_r = None
    cur_c = None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                cur_r = r
                cur_c = c
                grid[r][c] = 'a'
                break

    tar_r = None
    tar_c = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'E':
                tar_r = r
                tar_c = c
                grid[r][c] = 'z'
                break

    return bfs(grid, cur_r, cur_c, tar_r, tar_c)

def part2():
    grid = None
    with open("input.txt", "r") as f:
        line = list(map(lambda s: s.strip(), f.readlines()))
        grid = [list(w) for w in line]

    starts = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S' or grid[r][c] == 'a':
                starts.append((r, c))
                grid[r][c] = 'a'

    tar_r = None
    tar_c = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'E':
                tar_r = r
                tar_c = c
                grid[r][c] = 'z'
                break

    res = float('inf')

    for (cur_r, cur_c) in starts:
        res = min(res, bfs(grid, cur_r, cur_c, tar_r, tar_c))

    return res

if __name__ == "__main__":
    print(part1())
    print(part2())