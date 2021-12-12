from collections import defaultdict


def input(file_name):
    m = defaultdict(lambda: defaultdict(lambda: -1))
    with open(file_name) as f:
        l = 0
        for line in f:
            for k in range(0, len(line.strip())):
                m[l][k] = int(line[k])
            l += 1
        return m


def oob(r, c, octos):
    return r < 0 or r >= len(octos) or c < 0 or c >= len(octos[0])


def flash(octos, r, c, flashed):
    if flashed[r][c] == 1:
        return
    flashed[r][c] = 1

    adj = [
        (r - 1, c),
        (r - 1, c + 1),
        (r - 1, c - 1),
        (r, c + 1),
        (r, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
        (r + 1, c - 1),
    ]

    for a in adj:
        ar, ac = a
        if oob(ar, ac, octos):
            continue
        octos[ar][ac] += 1
        if octos[ar][ac] > 9 and not flashed[ar][ac]:
            flash(octos, ar, ac, flashed)


def evolve(octos, flashed):
    for r in range(len(octos)):
        for c in range(len(octos[0])):
            octos[r][c] += 1
    for r in range(len(octos)):
        for c in range(len(octos[0])):
            if octos[r][c] > 9:
                flash(octos, r, c, flashed)
    flash_count = 0
    for r in range(len(octos)):
        for c in range(len(octos[0])):
            if flashed[r][c] == 1:
                flash_count += 1
                octos[r][c] = 0
            flashed[r][c] = 0
    return flash_count


def main():
    octos = input("input.txt")
    flashed = defaultdict(lambda: defaultdict(lambda: 0))
    flash_count = 0
    flash_party = False
    step = 1
    while not flash_party:
        d_flash = evolve(octos, flashed)
        flash_count += d_flash
        if d_flash == len(octos) * len(octos[0]):
            flash_party = True
            print(f"all flashed at {step}")
            break
        step += 1


if __name__ == "__main__":
    main()
