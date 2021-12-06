from collections import defaultdict


class Board:
    def __init__(self, lines):
        self.board = [l.replace("  ", " ").split(" ") for l in lines]
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.checks = 0
        self.col_checks = defaultdict(lambda: 0)
        self.row_checks = defaultdict(lambda: 0)
        self.done = False

    def call(self, number):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if self.board[r][c] == number:
                    self.board[r][c] += "c"
                    self.checks += 1
                    self.col_checks[c] += 1
                    self.row_checks[r] += 1

    def check(self):
        if self.checks < 5:
            return False
        for r in range(0, self.rows):
            if self.row_checks[r] == 5 or self.row_checks[r] == 5:
                return True
        for c in range(0, self.cols):
            if self.col_checks[c] == 5 or self.col_checks[c] == 5:
                return True
        return False

    def sum_nchecked(self):
        sum = 0
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                sum += 0 if "c" in self.board[r][c] else int(self.board[r][c])
        return sum

    def mark_done(self):
        self.done = True

    def done(self):
        return self.done


def read_boards(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        calls = lines[0].split(",")
        blines = lines[1:]
        i = 1
        boards = []
        while i < len(blines):
            boards.append(Board(blines[i : i + 5]))
            i += 5 + 1  # newline
        return calls, boards


def main():
    winners = []
    calls, boards = read_boards("input.txt")
    for call in calls:
        for b in boards:
            if b.done:
                continue
            b.call(call)
            if b.check():
                b.mark_done()
                winners.append((b, call))
    board, call = winners[-1]
    print(board.sum_nchecked() * int(call))


if __name__ == "__main__":
    main()
