# write a program which accept one number and print square of that number
# 5
#25

def DisplaySquare(Value1):
    Square = Value1*Value1
    return Square
    
def main():
    print("enter the number:")
    No1 = int(input())

    Ret = DisplaySquare(No1)

    print("Square of that number is :",Ret)

if __name__ == "__main__":
    main()