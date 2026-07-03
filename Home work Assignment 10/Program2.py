# write a program which accept one number and sum of firsrt N natural numbers
# input    5
#  output 15

def SumNatural(Value1):
    Result = 0
    for i in range(1,Value1+1):
        Result = Result+i
    return Result
   


def main():
    print("Enter the number:")
    No1 = int(input())

    Ret = SumNatural(No1)

    print("Sum of Natural number is:",Ret)


if __name__ == "__main__":
    main()