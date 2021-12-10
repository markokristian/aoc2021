def input(file_name):
    with open(file_name) as f:
        return [f.strip() for f in f.readlines()]


def main():
    lines = [l for l in input("input.txt")]
    RtoL = {"}": "{", ")": "(", "]": "[", ">": "<"}
    LtoR = {"{": "}", "(": ")", "[": "]", "<": ">"}
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in lines:
        q = []
        for c in line:
            if c in LtoR.keys():
                q.append(c)
            else:
                l = q.pop()
                if l != RtoL[c]:
                    # corrupt line
                    q = []
                    break
        if len(q) > 0:
            score = 0
            for c in reversed(q):
                score *= 5
                score += points[LtoR[c]]
            scores.append(score)
    mid = int(len(scores) / 2 - 0.5)
    print(sorted(scores)[mid])


if __name__ == "__main__":
    main()


# count lefts and rights
# lefts - rights = missing amount of rights
# eg 5 missing
# just add 5 ))))), then run the corrupt check
