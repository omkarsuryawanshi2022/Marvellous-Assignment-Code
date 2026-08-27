import pandas as pd
import matplotlib.pyplot as plt

def Marvellous():

    data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'English': [78, 85, 92, 45, 120]
    }

    df = pd.DataFrame(data)

    plt.boxplot(df['English'])
    plt.title('English Marks Distribution')
    plt.ylabel('English Marks')
    plt.show()


def main():
    Marvellous()


if __name__ == "__main__":
    main()