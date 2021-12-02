def main():
    with open("input.txt") as f:
        lines = f.readlines()
        ops = [l for l in lines]
    h = 0
    d = 0
    aim = 0
    for op in ops:
        s = op.split(" ")
        dir, magn = s[0], int(s[1])

        if dir == "down":
            aim += magn
        if dir == "up":
            aim -= magn
        if dir == "forward":
            h += magn
            d += aim * magn

    print(h * d)


if __name__ == "__main__":
    main()
