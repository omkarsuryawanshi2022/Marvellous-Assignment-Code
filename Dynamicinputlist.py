

def main():
    size  = 0
    Arr = list()

    print("Enter the number of Element :")
    size = int(input())

    print("enter the element:")
    for i in range(size):
        no = int(input())

        Arr.append(no)

    print(Arr)

    
if __name__ == "__main__":
    main()