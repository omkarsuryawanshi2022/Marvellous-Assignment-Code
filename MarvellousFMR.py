
CheckEven = lambda No : (No % 2==0)

Increment = lambda No : No+1

Addition = lambda No1,No2: No1 + No2

def FilterX(Task,Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # checkeven(no)

        if(Ret == True):
            Result.append(no)
    return Result

def MApX(Task,Elements):
    Result =[]
    for no in Elements:
        Ret = Task(no)  # increment(no)

        Result.append(Ret)
    return Result

def ReduceX(Task,Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum


def main():
    Data = [13,12,8,10,11,20]

    print("Enput data is :",Data)

    FData = list(Xfilter(CheckEven,Data))

    MData = list(MApX(Increment,FData))

    print("Data After map:",MData)

    print("Data after filter :",FData)

    RData = ReduceX(Addition,MData)

    print("Data After Reduse is:",RData)

    
if __name__  == "__main__":
    main()
