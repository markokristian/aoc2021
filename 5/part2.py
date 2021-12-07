from collections import defaultdict
import copy


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


def read_lines(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return [Line(l.strip()) for l in lines]


def place(line, plane):
    if line.xs_same:
        max_y = max(line.a.y, line.b.y)
        min_y = min(line.a.y, line.b.y)
        for y in range(min_y, max_y + 1):
            plane[(line.a.x, y)] += 1
        return
    if line.ys_same:
        max_x = max(line.a.x, line.b.x)
        min_x = min(line.a.x, line.b.x)
        for x in range(min_x, max_x + 1):
            plane[(x, line.a.y)] += 1
        return
    if not line.xs_same and not line.ys_same:
        if line.a.x > line.b.x:
            tmp = copy.deepcopy(line.a)
            line.a = line.b
            line.b = tmp
        # down right
        if line.a.x < line.b.x and line.a.y < line.b.y:
            moves = zip(range(line.a.x, line.b.x + 1), range(line.a.y, line.b.y + 1))
            for x, y in moves:
                plane[(x, y)] += 1
            return
        # up right
        if line.a.x < line.b.x and line.a.y > line.b.y:
            moves = zip(
                range(line.a.x, line.b.x + 1), range(line.a.y, line.b.y - 1, -1)
            )
            for x, y in moves:
                plane[(x, y)] += 1
            return


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
