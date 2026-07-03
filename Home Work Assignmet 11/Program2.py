# write a program which accept one number and prints count of digits in that number 
#  input -  1234
#  output - 4

def CountDigit(No1):
    count = 0

    if No1 == 0:
        return 1

    No1 = abs(No1)   # Handle negative numbers

    while No1 > 0:
        count += 1
        No1 = No1 // 10

    return count
   


def main():
    print("Enter the number:")
    No1 = int(input())

    Ans = CountDigit(No1)
    print("Count of digits is:", Ans)

if __name__ == "__main__":
    main()