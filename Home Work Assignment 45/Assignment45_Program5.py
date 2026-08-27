import pandas as pd
import numpy as np

def Marvellous():

    data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Total': [260, 940, 100, 240, 390]
    }

    df = pd.DataFrame(data)

    df['Status'] = np.where(df['Total'] >= 250, 'pass','fail')

    
    print(df)


def main():

    Marvellous()


if __name__ == "__main__":
    main()