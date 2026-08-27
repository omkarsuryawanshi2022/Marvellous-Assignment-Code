import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    Data = {
        "Name":  ["Amit","Sagar","Pojja"],
        "Math":  [85,90,78],
        "Science":  [92,88,80],
        "English":  [75,85,82],
    }

    dobj = pd.DataFrame(Data)

    print(dobj.describe())

    dobj['Total'] = dobj['Math'] + dobj['Science'] + dobj['English']

    print("Total Count of sum is :")
    print(dobj)

    print("In Science Subject greater than 85 marks of student name is :")
    print(dobj[dobj['Science'] > 85])

    dobj.loc[dobj['Name'] == 'Pojja', 'Name'] = 'Po'

    print("Change name is :")
    print(dobj)

data2 = {
    'Name': ['Amit', 'Sagar', 'Pojja'],
    'Math': [np.nan, 80, 90],
    'Science': [90, np.nan, 55]
}

df = pd.DataFrame(data2)

print("Original DataFrame:")
print(df)

# Fill missing values with column mean
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())

print("\nDataFrame after filling missing values:")
print(df)



    
if __name__ =="__main__":
    main()