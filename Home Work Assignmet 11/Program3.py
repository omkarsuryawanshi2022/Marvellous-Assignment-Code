# Write a program which accepts one number and prints the sum of digits
# Input: 1234
# Output: 10

def SumOfDigit(No1):
    sum = 0

    No1 = abs(No1)   # Handle negative numbers

    while No1 > 0:
        digit = No1 % 10
        sum = sum + digit
        No1 = No1 // 10

    return sum


def main():
    print("Enter the number:")
    No1 = int(input())

    Ans = SumOfDigit(No1)
    print("Sum of digits is:", Ans)


if __name__ == "__main__":
    main()