import pandas as pd

def Marvellous():

    data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'math': [55, 94, 66, 88, 100]
    }

    df = pd.DataFrame(data)

    df['math_normalized'] = (
        df['math'] - df['math'].min()
    ) / (
        df['math'].max() - df['math'].min()
    )

    print(df)


def main():

    Marvellous()


if __name__ == "__main__":
    main()