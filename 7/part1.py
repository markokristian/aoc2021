from collections import defaultdict


def read_crabs(file_name):
    with open(file_name) as f:
        return [int(f) for f in f.readlines()[0].split(",")]


def main():
    crabs = read_crabs("input.txt")
    d = defaultdict(lambda: 0)
    for c in crabs:
        d[c] += 1

    dist_min = 1000000000
    for dest in d.keys():
        tot_dist = 0
        for source in d.keys():
            tot_dist += abs(int(source) - int(dest)) * d[source]
        if tot_dist < dist_min:
            dist_min = tot_dist

    print(dist_min)


if __name__ == "__main__":
    main()
