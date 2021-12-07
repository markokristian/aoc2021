from collections import defaultdict


def read_crabs(file_name):
    with open(file_name) as f:
        return [int(f) for f in f.readlines()[0].split(",")]


def main():
    crabs = read_crabs("input.txt")
    d = defaultdict(lambda: 0)
    for c in crabs:
        d[c] += 1

    fuel_min = 10000000000
    ks = d.keys()
    mink = min(ks)
    maxk = max(ks)
    for dest in range(mink, maxk + 1):
        tot_fuel = 0
        for source in d.keys():
            dist = abs(int(source) - int(dest))
            if dist == 0:
                continue
            tot_fuel += sum(range(1, dist + 1)) * d[source]

        if tot_fuel < fuel_min:
            fuel_min = tot_fuel

    print(fuel_min)


if __name__ == "__main__":
    main()
