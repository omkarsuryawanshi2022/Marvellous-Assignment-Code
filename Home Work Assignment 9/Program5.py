# Write a program which Accept one number and check whether it is Divisible by 3 and 5

def  CheckNumber(value1):

    if(value1 % 3 == 0 and value1 % 5 == 0):
        return True  
    else:
        return False

def main():

    print("Enter First number:")
    No1 =  int(input())

    Ret = CheckNumber(No1)

    if Ret == True:
        print("Number is Divisible by 3 and 5 :")
        
    else:
        print("Number is  Not Divisible by 3 and 5 :")


if __name__ == "__main__":
    main()