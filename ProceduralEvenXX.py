def CheckEven(No):
   return (No % 2 == 0)

def main():
    Value = int(input("Enter number:"))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("its Even number:")

    else:
        print("its Odd number:")



if __name__ == "__main__":
    main()