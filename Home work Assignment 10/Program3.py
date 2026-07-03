# write a program which accept one number and print Factorial of that number
# input    5
#  output 120

def Fatorial(Value1):
    Result = 1
    for iCnt in range(2, Value1+1):
        Result = Result*iCnt
    return  Result


def main():
    print("Enter the number:")
    No1 = int(input())

    Ret = Fatorial(No1)

    print("Factorial is:",Ret)


if __name__ == "__main__":
    main()