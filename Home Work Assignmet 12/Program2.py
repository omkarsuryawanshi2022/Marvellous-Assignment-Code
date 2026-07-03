# Write a program which accept one number and print its factors
#  input  12
# output  1 2 3 4 6 12 

def Factor(value):
    for i in range(1, value + 1):
        if value % i == 0:

            print(i, end=" ")

   
    
def main():
    print("Enter the character:")
    No1 = int(input())

    Ret= Factor(No1)

    print("Factors is :",Ret)
    
    
if __name__ == "__main__":
    main()