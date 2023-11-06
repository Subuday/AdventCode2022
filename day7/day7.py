from collections import deque

class Node:
    def __init__(self, name, parent, size=0, is_file=False):
        self.name = name
        self.parent = parent
        self.size = size
        self.is_file = is_file
        self.children = []

def buildTree() -> Node:
    output = None
    with open("input.txt", "r") as f:
        output = map(lambda s: s.strip(), f.readlines())

    root = None
    cur = None
    for line in output:
        parts = line.split(" ")
        if parts[0] == "$":
            cmd = parts[1]
            if cmd == "cd":
                folder = parts[2]
                if folder == "/":
                    root = Node("/", None)
                    cur = root
                elif folder == "..":
                    cur = cur.parent
                else:
                    node = Node(folder, cur)
                    cur.children.append(node)
                    cur = node
        else:
            ls_type = parts[0]
            if ls_type != "dir":
                node = Node(name=parts[1], parent=cur, size=int(parts[0]), is_file=True)
                cur.children.append(node)


    def dfs(n):
        if n is None:
            return 0
        if n.is_file:
            return n.size

        for c in n.children:
            n.size += dfs(c)

        return n.size

    root.size = dfs(root)

    return root

def part1():
    root = buildTree()

    res = [0]
    def dfs(n):
        if n is None or n.is_file:
            return

        if n.size < 100_000:
            res[0] += n.size

        for c in n.children:
            dfs(c)

    dfs(root)

    return res[0]


def part2():
    root = buildTree()

    total_space = 70_000_000
    used_space = root.size
    free_space = total_space - used_space
    need_space = 30_000_000 - free_space

    res = float("inf")
    q = deque([root])
    while q:
        n = q.popleft()
        if n is None or n.is_file:
            continue
        if n.size >= need_space:
            res = min(res, n.size)

        for c in n.children:
            q.append(c)

    return res

if __name__ == "__main__":
    print(part1())
    print(part2())