def main():
    with open("input.txt") as f:
        lines = f.readlines()
        numbers = [int(l) for l in lines]

    previous = 1000000000
    k = 0
    for n in range(0, len(numbers)):
        if n + 2 >= len(numbers):
            break
        next = numbers[n] + numbers[n + 1] + numbers[n + 2]
        if next > previous:
            k += 1
        previous = next
    print(k)


if __name__ == "__main__":
    main()
