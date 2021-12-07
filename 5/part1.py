from collections import defaultdict


class Point:
    def __init__(self, foo) -> None:
        self.x = int(foo[0])
        self.y = int(foo[1])
        self.desc = f"{self.x},{self.y}"


class Line:
    def __init__(self, line) -> None:
        s = line.split(" -> ")
        self.a = Point(s[0].split(","))
        self.b = Point(s[1].split(","))
        self.desc = f"{self.a.desc} -> {self.b.desc}"
        self.xs_same = self.a.x == self.b.x
        self.ys_same = self.a.y == self.b.y

    def is_hor_ver(self):
        return self.xs_same or self.ys_same


def read_lines(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return [Line(l.strip()) for l in lines]


def place(line, plane):
    if not line.is_hor_ver():
        return
    if line.xs_same:
        ma = max(line.a.y, line.b.y)
        mi = min(line.a.y, line.b.y)
        for y in range(mi, ma + 1):
            plane[(line.a.x, y)] += 1
    if line.ys_same:
        ma = max(line.a.x, line.b.x)
        mi = min(line.a.x, line.b.x)
        for x in range(mi, ma + 1):
            plane[(x, line.a.y)] += 1


def main():
    ls = read_lines("input.txt")
    plane = defaultdict(lambda: 0)
    c = 0
    for l in ls:
        place(l, plane)
    for v in plane.values():
        if v >= 2:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
