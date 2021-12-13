from collections import defaultdict


def input(file_name):
    with open(file_name) as f:
        paper = defaultdict(lambda: defaultdict(lambda: "."))
        folds = []
        for line in f:
            if line == "\n":
                continue
            if line.startswith("fold"):
                k, v = line.split(" ")[2].rstrip().split("=")
                folds.append({k: int(v)})
                continue
            s = line.rstrip().split(",")
            paper[int(s[0])][int(s[1])] = "#"
        return paper, folds


def maxes(paper):
    my, mx = 0, max(paper.keys())
    for x in paper.keys():
        my = max(my, max(paper[x].keys()))
    miny, minx = 1000000, min(paper.keys())
    for x in paper.keys():
        miny = min(miny, min(paper[x].keys()))
    return minx, mx, miny, my


def print_paper(paper):
    # not sure if non-mid folds are allowed? probably not.
    _, maxx, _, maxy = maxes(paper)
    for y in range(0, maxy + 1):
        print(f"{y:>2} " + "".join([paper[x][y] for x in range(0, maxx + 1)]))
        # print("".join([f"({x:>2},{y:>2})" for x in range(0, mx + 1)]))


def main():
    paper, folds = input("input.txt")

    def foldx(paper, fold):
        paper2 = defaultdict(lambda: defaultdict(lambda: "."))
        _, maxx, _, maxy = maxes(paper)
        for x in range(0, maxx + 1):
            for y in range(0, maxy + 1):
                if x < fold:
                    paper2[x][y] = paper[x][y]
                    continue
                dist = abs(fold - x)
                newx = fold - dist
                if paper[x][y] == "#":
                    paper2[newx][y] = paper[x][y]
        return paper2

    def foldy(paper, fold):
        paper2 = defaultdict(lambda: defaultdict(lambda: "."))
        _, maxx, _, maxy = maxes(paper)
        for x in range(0, maxx + 1):
            for y in range(0, maxy + 1):
                if y < fold:
                    paper2[x][y] = paper[x][y]
                    continue
                dist = abs(fold - y)
                newy = fold - dist
                if paper[x][y] == "#":
                    paper2[x][newy] = paper[x][y]
        return paper2

    def fold(paper, folds):
        for fold in folds:
            if "x" in fold:
                paper = foldx(paper, fold["x"])
            if "y" in fold:
                paper = foldy(paper, fold["y"])
        return paper

    folded = fold(paper, folds)
    print_paper(folded)


if __name__ == "__main__":
    main()
