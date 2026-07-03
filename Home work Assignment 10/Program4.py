def DisplayEven(Value1):
    for iCnt in range(2,Value1,2):
            
            print(iCnt)

def main():
    print("Enter the number:")
    No1 = int(input())

    DisplayEven(No1)
    

if __name__ == "__main__":
    main()
