from math import inf
from collections import defaultdict
from itertools import product

def build_graph():
    graph = {}
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(' ')
            graph[parts[1]] = list(map(lambda x: x.strip(','), parts[9:]))
    return graph

def build_rates():
    rates = {}
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(' ')
            rates[parts[1]] = parts[4].split('=')[1].strip(';')
    return rates

def floyd_warshall(graph):
    distance = defaultdict(lambda: defaultdict(lambda: inf))

    for a, bs in graph.items():
        distance[a][a] = 0

        for b in bs:
            distance[a][b] = 1
            distance[b][b] = 1

    # a is the intermediate node
    # b is the source node
    # c is the destination node
    for a, b, c in product(graph, graph, graph):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance


def solutions(distance, rates, valves, time=30, cur='AA', chosen={}):
    res = [chosen]

    # We can't reach any other valve in less than 2m, as it would take minimum
    # 1m to reach it plus 1m to open it, and therefore it'd be stay open for 0m.
    if time < 2:
        return res

    # For all the valves we can currently choose
    for nxt in valves:
        # Choosing this valve will take distance[cur][nxt] to reach it, plus 1m to open it
        new_time   = time - (distance[cur][nxt] + 1)
        # Choose this valve, it will stay open exactly for new_time (i.e. the time
        # we have now minus the time it takes to reach and open it).
        new_chosen = chosen.copy()
        new_chosen.update({nxt: new_time})
        # The new valves to choose from will not include this one
        new_valves = valves - {nxt}
        # Collect all possible choices having taken this valve
        res += solutions(distance, rates, new_valves, new_time, nxt, new_chosen)

    return res

def part1():
    graph = build_graph()
    rates = build_rates()
    distance = floyd_warshall(graph)
    valves = set(graph.keys())
    good_vales = valves.copy()
    for v in valves:
        if rates[v] == '0':
            good_vales.remove(v)
    sols = solutions(distance, rates, good_vales)

    res = 0
    for sol in sols:
        r = 0
        for v, t in sol.items():
            if t > 0:
                r += int(rates[v]) * t
        res = max(res, r)

    return res


def part2():
    graph = build_graph()
    rates = build_rates()
    distance = floyd_warshall(graph)
    valves = set(graph.keys())
    good_vales = valves.copy()
    for v in valves:
        if rates[v] == '0':
            good_vales.remove(v)
    sols = solutions(distance, rates, good_vales, 26)

    maxscore = defaultdict(int)
    for s in sols:
        score = 0
        for v, t in s.items():
            if t > 0:
                score += int(rates[v]) * t

        k = frozenset(s)
        if score > maxscore[k]:
            maxscore[k] = score

    res = 0
    for s1, score1 in maxscore.items():
        for s2, score2 in maxscore.items():
            if len(s1.intersection(s2)) == 0:
                cur = score1 + score2
                if cur > res:
                    res = cur


    return res


if __name__ == "__main__":
    print(part1())
    print(part2())