# Write a program which accepts one number and print reverse of that number
# Input:  123
# Output: 321

def ReverseNumber(No1):
    Rev = 0

    No1 = abs(No1)   # Handle negative numbers
    while No1 >0:
        Digit = No1 % 10
        Rev =  Rev*10+Digit
        No1 = No1 // 10
    return Rev


def main():
    print("Enter the number:")
    No1 = int(input())

    Ans = ReverseNumber(No1)
    print("Reverse number is :", Ans)


if __name__ == "__main__":
    main()