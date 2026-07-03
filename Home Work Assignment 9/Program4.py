# Write a program which Accept one number and print cube of that number

def DisplayCube(Value1):
    # 6 = 6*6*6
    # 6 = 6*1 = 6
    # 6 = 6*6 = 36
    # 6 = 36*6 = 216

    Value1 = Value1*Value1*Value1
    return Value1
  
def main():
    print("enter the number:")
    No1 = int(input())

    Ret = DisplayCube(No1)

    print("Square of that number is :",Ret)

if __name__ == "__main__":
    main()