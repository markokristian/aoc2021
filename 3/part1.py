from collections import defaultdict


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        bitlines = [l.rstrip() for l in lines]

    sums = defaultdict(lambda: 0)
    n = len(bitlines)
    half = n / 2
    bits = len(bitlines[0])
    for bitline in bitlines:
        for i in range(0, len(bitline)):
            sums[i] += int(bitline[i])

    gamma = ""
    for v in sums.values():
        gamma += "1" if v > half else "0"

    gamma = int(gamma, 2)
    mask = pow(2, bits) - 1
    epsilon = gamma ^ mask

    print("gamma", bin(gamma))
    print("mask", bin(mask))
    print("epsil", bin(epsilon))
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
