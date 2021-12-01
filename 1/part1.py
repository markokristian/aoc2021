def main():
    with open("input.txt") as f:
        lines = f.readlines()
        numbers = [int(l) for l in lines]

    k = 0
    for n in range(1, len(numbers)):
        if numbers[n] > numbers[n - 1]:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
