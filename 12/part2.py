from collections import defaultdict
import copy


def input(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.rstrip().split("-")


def small_full(path):
    for n, v in path.items():
        if v == 2 and n.islower() and n not in ["start", "end"]:
            return True
    return False


def dfs(g, node, path):
    path[node] += 1
    if node == "end":
        return 1
    sum = 0
    for adj in g[node]:
        if adj.islower() and path[adj] == 2 and adj != "end":
            continue
        if adj.islower() and path[adj] == 1 and adj != "end" and small_full(path):
            continue
        sum += dfs(g, adj, copy.deepcopy(path))
    return sum


def main():
    g = defaultdict(lambda: set())
    for l, r in input("test3.txt"):
        if l != "end" and r != "start":
            g[l].add(r)
        if r != "end" and l != "start":
            g[r].add(l)

    n_paths = 0
    for adj in g["start"]:
        path = defaultdict(lambda: 0)
        path["start"] = 1
        n_paths += dfs(g, adj, path)
    print(n_paths)


if __name__ == "__main__":
    main()
