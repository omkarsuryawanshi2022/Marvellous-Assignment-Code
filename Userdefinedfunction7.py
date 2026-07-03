def Calculation(No1,No2):
    Mult = No1 * No2
    Div = No1 / No2
    return Mult,Div

def main():
    value1 = int(input("Enter the first number :"))
    value2 = int(input("Enter the Second number :"))

    Ret1 ,Ret2 = Calculation(value1,value2)

    print("Multiplication is :",Ret1)

    print("Division is :",Ret2)


 
if __name__  == "__main__":
    main()

    