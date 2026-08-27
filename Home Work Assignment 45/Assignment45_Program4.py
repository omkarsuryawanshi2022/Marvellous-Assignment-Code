import matplotlib.pyplot as plt

def DisplayMarks ():
    Subject = ['Math','Science','marathi','History','Sanskruth']
    Marks = [50,60,70,80,90]

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    plt.figure(figsize=(6,6))
    plt.pie(

        Marks,
        labels=Subject,
        startangle=140,
        colors=colors,
        shadow=True
    )

    plt.title("Sagar's Subject Marks Distribution", fontsize = 14, fontweight ='bold')

    plt.show()
    plt.legend()


    
def main():

    DisplayMarks ()

if __name__ == "__main__":
    main()