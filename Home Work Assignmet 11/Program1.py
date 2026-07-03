def CheckPrime(No1):
    if No1 <= 1:
        return False

    for i in range(2, int(No1 ** 0.5) + 1):
        if No1 % i == 0:
            return False

    return True


def main():
    print("Enter the number:")
    No1 = int(input())

    if CheckPrime(No1):
        print("It is a Prime number")
    else:
        print("It is not a Prime number")


if __name__ == "__main__":
    main()