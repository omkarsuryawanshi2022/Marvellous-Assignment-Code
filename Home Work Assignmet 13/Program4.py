# Write a program which accepts one number and prints its binary equivalent

def DecimalToBinary(No):
    if No == 0:
        return "0"

    binary = ""

    No = abs(No)   # handle negative numbers 

    while No > 0:
        rem = No % 2
        binary = str(rem) + binary
        No = No // 2

    return binary


def main():
    print("Enter the number:")
    No = int(input())

    result = DecimalToBinary(No)

    print("Binary equivalent is:", result)


if __name__ == "__main__":
    main()