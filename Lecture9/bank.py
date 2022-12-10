balance = 0


def main():
    print("Balance:", balance)
    deposit(1000)
    whitdraw(50)
    print("Balance:", balance)


def deposit(n):
    # define global var in a func
    global balance
    balance += n


def whitdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
