def main():
    with open("input.txt") as f:
        lines = f.readlines()
        bitlines = sorted([l.rstrip() for l in lines], reverse=True)

    def prune(what, c, bitlines):
        if len(bitlines) == 1:
            return bitlines
        return [l for l in bitlines if l[c] != what]

    def check(col, bitlines):
        n = len(bitlines)
        if n == 1:
            m = bitlines[0][col]
            return m, "0" if m == "1" else "0"
        ones = 0
        for r in range(0, n):
            bit = bitlines[r][col]
            ones += int(bit)
            zeros = n - ones
            if r > 0 and bit != bitlines[r - 1][col]:
                if ones >= zeros:
                    return "1", "0"
                else:
                    return "0", "1"

    def tail(col, b1, b2):
        if col == len(b1[0]):
            return b1, b2
        _, l1 = check(col, b1)
        m2, _ = check(col, b2)
        b1 = prune(l1, col, b1)
        b2 = prune(m2, col, b2)
        return tail(col + 1, b1, b2)

    b1, b2 = tail(0, bitlines, bitlines)

    o2_rating = int(b1[0], 2)
    co2_rating = int(b2[0], 2)
    print(o2_rating, co2_rating, o2_rating * co2_rating)


if __name__ == "__main__":
    main()
