# Write a program which accepts two numbers and prints
# Addition, Subtraction, Multiplication, and Division

def Arithmetic(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2

    if No2 != 0:
        Div = No1 / No2
    else:
        Div = "Division by zero is not possible"

    return Add, Sub, Mul, Div


def main():
    print("Enter the first number:")
    No1 = int(input())

    print("Enter the second number:")
    No2 = int(input())

    Add, Sub, Mul, Div = Arithmetic(No1, No2)

    print("Addition       :", Add)
    print("Subtraction    :", Sub)
    print("Multiplication :", Mul)
    print("Division       :", Div)


if __name__ == "__main__":
    main()