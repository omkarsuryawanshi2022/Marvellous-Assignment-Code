# Write a program which accepts one number and check whether it is palindrome or not
# Input:  121
# Output: Palindrome

def CheckPalindrome(No1):
    original  = abs(No1) # Store original vlaue
    Temp = original
    Rev = 0

    while Temp > 0:
        Digit = Temp % 10
        Rev = Rev * 10 + Digit
        Temp = Temp // 10

        if original == Rev:
            return True
        else:
            return False
   

def main():
    print("Enter the number:")
    No1 = int(input())

    Ans = CheckPalindrome(No1)
    
    if Ans:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()