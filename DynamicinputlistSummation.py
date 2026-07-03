
def Summation(Data):
    Sum = 0
    for no in Data:
        Sum = Sum+ no

    return Sum

def main():
    size  = 0
    Arr = list()

    print("Enter the number of Element :")
    size = int(input())

    print("enter the element:")
    for i in range(size):
        no = int(input())

        Arr.append(no)

    Ret = Summation(Arr)

    print("Summation is :",Ret)

    
if __name__ == "__main__":
    main()