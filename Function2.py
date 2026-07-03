def Addition(No1,No2):
    Ans = 0

    Ans = No1 +No2
    return Ans


def main():
    print("Enter the first number:")
    value1 = int(input())

    print("Enter the second number:")
    value2 = int(input())

    Ret = Addition(value1 ,value2)
    print("Addition id :",Ret)


if __name__ == "__main__":
    main()
