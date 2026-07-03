from Marvellous import Addition

def main():
    print("Enter the first number:")
    value1 = int(input())

    print("Enter the second number:")
    value2 = int(input())

    Ret = Addition(value1 ,value2)

    print("Addition id :",Ret)

    Ret = Substraction(value1,value2)  # Error

    print("Substraction is:",Ret)


if __name__ == "__main__":
    main()
