from collections import defaultdict
from pprint import pprint
import math


def input(file_name):
    m = defaultdict(lambda: defaultdict(lambda: 42))
    with open(file_name) as f:
        l = 0
        for line in f:
            for k in range(0, len(line.strip())):
                m[l][k] = int(line[k])
            l += 1
        return m


def sz(r, c):
    v = hmap[r][c]

    if v in [9, 42, -1]:
        return 0

    # visit
    hmap[r][c] = -1
    size = 1
    size += sz(r - 1, c)
    size += sz(r + 1, c)
    size += sz(r, c - 1)
    size += sz(r, c + 1)

    return size


def main():
    basins = []
    for r in range(0, len(hmap)):
        for c in range(0, len(hmap[0])):
            v = hmap[r][c]
            if (
                v < hmap[r - 1][c]
                and v < hmap[r + 1][c]
                and v < hmap[r][c - 1]
                and v < hmap[r][c + 1]
            ):
                size = sz(r, c)
                basins.append(size)

    pprint(math.prod(sorted(basins, reverse=True)[:3]))


hmap = input("input.txt")
if __name__ == "__main__":
    main()
