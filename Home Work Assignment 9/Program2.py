# write aprogram which contain one function CheckGretter() that Accept two number and prints the gretter number
def  CheckGretter(value1,value2):
    if(value1>value2):
        return value1  
    else:
        return value2

def main():

    print("Enter First number:")
    No1 =  int(input())

    print("enter the Second Number:")
    No2 = int(input())

    Ret = CheckGretter(No1,No2)

    print("Largest number is :",Ret)

if __name__ == "__main__":
    main()