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
    dobj["Total"] = dobj[["Math","Science","English"]].sum(axis=1)

    print("Total Count of sum is :\n",dobj)

    Filtar_Df = dobj[dobj["Science"]> 85]

    print("In Science Subject gretter than 85 markrs of student name is :\n",Filtar_Df)

if __name__ =="__main__":
    main()