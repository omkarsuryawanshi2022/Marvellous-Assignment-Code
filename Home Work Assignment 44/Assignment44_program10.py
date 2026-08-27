import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    Data = {
        "Name": ["Amit", "Sagar", "Pojja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
    }

    dobj = pd.DataFrame(Data)

    print("Original DataFrame:")
    print(dobj)

    print("\nDataFrame Description:")
    print(dobj.describe())

    dobj['Total'] = dobj['Math'] + dobj['Science'] + dobj['English']

    print("\nTotal Count of sum is:")
    print(dobj)

    print("\nIn Science Subject greater than 85 marks:")
    print(dobj[dobj['Science'] > 85])

    dobj.loc[dobj['Name'] == 'Pojja', 'Name'] = 'Po'

    print("\nChange name is:")
    print(dobj)

    # Drop English column
    dobj.drop(columns=['English'], inplace=True)

    print("\nDataFrame After dropping English Column:")
    print(dobj)


if __name__ == "__main__":
    main()