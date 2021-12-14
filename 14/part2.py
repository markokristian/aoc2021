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

    # why even bother creating the string...
    elems, segments = Counter(), Counter()
    for pos in range(len(tpl) - 1):
        elems[tpl[pos]] += 1
        segments[tpl[pos] + tpl[pos + 1]] += 1
    elems[tpl[-1]] += 1

    for _ in range(40):
        segments_at_step = segments.copy()
        # print(segments_at_step)
        # print("---------------")
        for s, cnt in segments_at_step.items():
            between = replacements[s]
            elems[between] += cnt
            segments[s[0] + between] += cnt
            segments[between + s[1]] += cnt
            segments[s] -= cnt  # eg CH -> B, segment vanishes
    print(
        elems.most_common()[0][1] - elems.most_common()[-1][1],
    )


if __name__ == "__main__":
    main()
