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
