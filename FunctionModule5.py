from Marvellous import *

def main():
    print("Enter the first number:")
    value1 = int(input())

    print("Enter the second number:")
    value2 = int(input())

    Ret = Addition(value1 ,value2)

    print("Addition id :",Ret)

    Ret = Substraction(value1 ,value2)

    print("Substraction id :",Ret)

    Ret = Multiplication(value1 ,value2)

    print("Multiplication id :",Ret)

    Ret = Division(value1 ,value2)

    print("Division id :",Ret)


if __name__ == "__main__":
    main()
