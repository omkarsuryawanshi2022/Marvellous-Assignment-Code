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

    Amit  = dobj[dobj['Name']  == 'Amit'].iloc[0]

    plt.plot(
        ['Math','Science','English'],
        [Amit['Math'], Amit['Science'],Amit['English']],
         
         marker = "o",           
         linestyle = "--",
         linewidth = 2,
         markersize = 7,
         label = "Amit Marks"
    )

    plt.title("Amit Marks Across All Subjects")
    plt.xlabel("Subject")
    plt.ylabel("Marks")

    plt.grid(True)
    plt.legend()

    plt.show()



    
if __name__ =="__main__":
    main()