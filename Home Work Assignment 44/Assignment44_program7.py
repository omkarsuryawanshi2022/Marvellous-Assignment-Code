from matplotlib import category
import pandas as pd
import matplotlib.pyplot as plt


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

    Sorted_df = dobj.sort_values(by='Total', ascending=False)

    print("Sorted DataFrame in desending ordar :")
    print(Sorted_df)

    plt.figure(figsize= (8,5))

    plt.bar(
        Sorted_df['Name'],
        Sorted_df['Total'],
        color = 'skyblue',
        edgecolor = 'black',
        width=0.6
    )

    plt.title('Student Total Marks')
    plt.xlabel('Student')
    plt.ylabel('Total Marks')

    plt.show()


    
if __name__ =="__main__":
    main()