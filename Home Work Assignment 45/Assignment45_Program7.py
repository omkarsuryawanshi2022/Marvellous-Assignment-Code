import pandas as pd
import numpy as np

def Marvellous():

   data = {

       'TV': [230.1, 44.5, 17.2, 151.5, 180.8],
        'Radio': [37.8, 39.3, 45.9, 41.3, 10.8],
        'Newspaper': [69.2, 45.1, 69.3, 58.5, 58.4],
        'Sales': [22.1, 10.4, 12.0, 16.5, 17.9]
   }

   df = pd.DataFrame(data)

   df.to_csv('Advertising.csv', index = False)

   print(df)
   


def main():

    Marvellous()


if __name__ == "__main__":
    main()