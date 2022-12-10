def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)


def sheep(n: int):
    for i in range(n):
        # one value at the time
        yield "🐐" * i


if __name__ == "__main__":
    main()
