def input(file_name):
    with open(file_name) as f:
        return [f.strip() for f in f.readlines()]


def main():
    lines = [l for l in input("input.txt")]
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    RtoL = {"}": "{", ")": "(", "]": "[", ">": "<"}
    LtoR = {"{": "}", "(": ")", "[": "]", "<": ">"}
    for line in lines:
        q = []
        for c in line:
            if c in LtoR.keys():
                q.append(c)
            else:
                l = q.pop()
                if l != RtoL[c]:
                    # print(line, f"Expected {LtoR[l]}, but found {c} instead")
                    score += points[c]
    print(score)


if __name__ == "__main__":
    main()
