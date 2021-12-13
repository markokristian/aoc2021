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


def main():
    paper, folds = input("input.txt")
    fold = folds[0]["x"]
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

    _, maxx, _, maxy = maxes(paper2)
    sum = 0
    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            sum += 1 if paper2[x][y] == "#" else 0
    print(sum)


if __name__ == "__main__":
    main()
