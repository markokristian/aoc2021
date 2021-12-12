from collections import defaultdict
import copy


def input(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.rstrip().split("-")


def dfs(g, node, path):
    path.append(node)
    if node == "end":
        # print("path", node, path)
        return 1
    sum = 0
    for adj in g[node]:
        if adj.islower() and adj in path and adj != "end":
            continue
        sum += dfs(g, adj, copy.deepcopy(path))
    return sum


def main():
    g = defaultdict(lambda: set())
    for l, r in input("test3.txt"):
        if l != "end":
            g[l].add(r)
        if r != "end":
            g[r].add(l)

    def prune(g):
        waste = set()
        for n, adj in g.items():
            p = adj.pop()
            if (
                len(adj) == 0
                and p.islower()
                and n.islower()
                and n not in ["start", "end"]
            ):  # n is 'd'
                waste.add(n)
            adj.add(p)
        for w in waste:
            del g[w]
        for n, adj in g.items():
            g[n] -= waste
        return g

    g = prune(g)
    n_paths = 0
    for adj in g["start"]:
        n_paths += dfs(g, adj, path=["start"])
    print(n_paths)


if __name__ == "__main__":
    main()
