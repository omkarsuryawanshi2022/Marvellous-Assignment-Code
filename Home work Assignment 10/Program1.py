# write a program which accept one number and print multiplication table of that number:
# input 5
# 5 10 15 20 25 30 35 40 45 50
def DisplayMult(Value1):
    for i in range(1,11):
        print(Value1*i)

def main():
    print("Enter the number:")
    No1 = int(input())

    DisplayMult(No1)


if __name__ == "__main__":
    main()