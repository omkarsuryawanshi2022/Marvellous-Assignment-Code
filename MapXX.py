CheckEven = lambda No:(No % 2==0)

Increment = lambda No:No+1

def main():
    Data = [13,12,8,10,11,20]

    print("Enput data is :",Data)

    FData = list(filter(CheckEven,Data))

    MData = list(map(Increment,FData))

    print("Data After map:",MData)

    print("Data after filter :",FData)
if __name__  == "__main__":
    main()
