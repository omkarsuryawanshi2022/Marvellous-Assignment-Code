import pandas as pd

def main():
    Data = {
        "Name":  ["Amit","Sagar","Pojja"],
        "Math":  [85,90,78],
        "Science":  [92,88,80],
        "English":  [75,85,82],
    }

    dobj = pd.DataFrame(Data)

    print(dobj.describe())
    

    #print(dobj[["Name","Math","Science","English"]])

if __name__ =="__main__":
    main()