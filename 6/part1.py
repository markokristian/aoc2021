class Fish:
    def __init__(self, timer) -> None:
        self.timer = timer

    def step(self, pond):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            pond.add()

    def desc(self):
        return f"{self.timer}"


class Pond:
    def __init__(self, fish) -> None:
        self.fish = fish

    def add(self):
        self.fish.append(Fish(9))

    def step(self):
        for f in self.fish:
            f.step(self)

    def desc(self):
        return ",".join([f.desc() for f in self.fish])


def read_fish(file_name):
    with open(file_name) as f:
        init = [int(f) for f in f.readlines()[0].split(",")]
        for i in init:
            yield Fish(i)


def main():
    fish = read_fish("input.txt")
    pond = Pond(list(fish))  # mem!
    days = 80

    for d in range(0, days):
        pond.step()
        # print(f"After {d + 1}: {pond.desc()}")

    print(len(pond.fish))


if __name__ == "__main__":
    main()
