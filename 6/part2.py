from collections import defaultdict
import json


class Fish:
    def __init__(self, timer) -> None:
        self.timer = timer

    def desc(self):
        return f"{self.timer}"


class Pond:
    def __init__(self, fish) -> None:
        self.fish_ages = defaultdict(lambda: 0)
        for f in fish:
            self.fish_ages[f.timer] += 1

    def nfish(self):
        return sum(self.fish_ages.values())

    def step(self):
        ops = []
        for age in range(0, 9):
            if age == 0:
                # -1 -> 6
                n_with_age = self.fish_ages[0]
                if n_with_age == 0:
                    continue
                ops.append((0, -n_with_age))
                ops.append((6, +n_with_age))
                # born!
                ops.append((8, +n_with_age))
            else:
                n_with_age = self.fish_ages[age]
                if n_with_age == 0:
                    continue
                ops.append((age, -n_with_age))
                ops.append((age - 1, +n_with_age))

        for op in ops:
            self.fish_ages[op[0]] += op[1]

    def desc(self):
        return json.dumps(self.fish_ages)


def read_fish(file_name):
    with open(file_name) as f:
        init = [int(f) for f in f.readlines()[0].split(",")]
        for i in init:
            yield Fish(i)


def main():
    fish = read_fish("input.txt")
    pond = Pond(list(fish))
    days = 256

    for d in range(0, days):
        pond.step()
        print(f"After {d + 1}: {pond.desc()}")

    print(pond.nfish())


if __name__ == "__main__":
    main()
