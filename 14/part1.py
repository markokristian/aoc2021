from collections import Counter


def input(file_name):
    with open(file_name) as f:
        for line in f:
            if line == "\n":
                continue
            if "->" in line:
                yield line.rstrip().split(" -> ")
            else:
                tpl = line.rstrip()
                yield tpl


def main():
    data = list(input("input.txt"))
    replacements = {m[0]: m[1] for m in data[1:]}
    tpl = data[0]

    def match(tpl, replacements):
        s = ""
        for pos in range(len(tpl) - 1):
            sub = tpl[pos] + tpl[pos + 1]
            if sub in replacements:
                between = replacements[sub]
                s += sub[0] + between
            else:
                s += sub[0]
        s += tpl[-1]
        return s

    s = tpl
    for _ in range(10):
        s = match(s, replacements)
    elems = Counter(s)
    print("len", len(s))
    print(
        elems.most_common()[0][1] - elems.most_common()[-1][1],
    )


if __name__ == "__main__":
    main()
