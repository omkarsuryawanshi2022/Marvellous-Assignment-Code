CheckEven = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter number:"))

    Ret = CheckEven(Value)   # Ret =  (value % 2 == 0)

    if(Ret == True):
        print("its Even number:")

    else:
        print("its Odd number:")



if __name__ == "__main__":
    main()