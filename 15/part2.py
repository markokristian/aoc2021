import heapq
import copy


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


def grow(g):
    width = max(g)[0] + 1  # 9 + 1
    height = max(g)[1] + 1
    cp = copy.copy(g)
    # 5 times right
    for k in range(1, 5):
        for pos in g:
            x, y = pos
            v = g[pos] + k * 1
            w = 1 if abs(v - 9) == 0 else abs(v - 9)
            cp[(x + width * k, y)] = w if v > 9 else v
    del g
    dp = copy.copy(cp)
    # 5 times down
    for k in range(1, 5):
        for pos in cp:
            x, y = pos
            v = cp[pos] + k * 1
            w = 1 if abs(v - 9) == 0 else abs(v - 9)
            dp[(x, y + height * k)] = w if v > 9 else v
    del cp
    return dp


def print_g(g):
    maxx, maxy = max(g)
    for y in range(0, maxy + 1):
        s = "".join([str(g[(x, y)]) for x in range(0, maxx + 1)])
        print(s)


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
    g = dict(input("test3.txt"))
    g = grow(g)
    # print_g(g)
    m = max(g)
    print(dijkstra(g, (0, 0), m, m))


if __name__ == "__main__":
    main()
