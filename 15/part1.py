import heapq


def input(file_name):
    with open(file_name) as f:
        y = 0
        x = 0
        for line in f:
            for cost in line.rstrip():
                yield ((x, y), int(cost))
                x += 1
            y += 1
            x = 0


def adj(pos, g, max):
    x, y = pos
    a = [
        None if x == 0 else (x - 1, y),
        None if y == max[1] else (x, y + 1),
        None if y == 0 else (x, y - 1),
        None if x == max[0] else (x + 1, y),
    ]
    return [(pos, g[pos]) for pos in a if pos is not None]


# tweaked https://stackoverflow.com/a/58833232
def dijkstra(g, start, goal, max):
    q = []
    d = {k: 100000000 for k in g.keys()}
    p = {}
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        last_cost, current = heapq.heappop(q)
        for pos, cost in adj(current, g, max):
            dist = last_cost + cost
            if dist < d[pos]:
                d[pos] = dist
                p[pos] = current
                heapq.heappush(q, (dist, pos))
    return d[goal]


def main():
    g = dict(input("input.txt"))
    m = max(g)
    print(dijkstra(g, (0, 0), m, m))


if __name__ == "__main__":
    main()
