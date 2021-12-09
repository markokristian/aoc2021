from collections import defaultdict


def input(file_name):
    m = defaultdict(lambda: defaultdict(lambda: 42))
    with open(file_name) as f:
        l = 0
        for line in f:
            for k in range(0, len(line.strip())):
                m[l][k] = int(line[k])
            l += 1
        return m


def main():
    hmap = input("input.txt")
    t = []
    for n in range(0, len(hmap)):
        for k in range(0, len(hmap[0])):
            v = hmap[n][k]
            if (
                v < hmap[n - 1][k]
                and v < hmap[n + 1][k]
                and v < hmap[n][k - 1]
                and v < hmap[n][k + 1]
            ):
                t.append(v + 1)
    s = sum([int(num) for num in t])
    print(s)


if __name__ == "__main__":
    main()
