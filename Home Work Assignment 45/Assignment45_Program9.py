import pandas as pd

def main():
    df = pd.DataFrame({"math":[90,85], "Science": [88,62]})

    print("after:\n",df)

    df.rename(columns={"math":"mathematics"},inplace=True)

    print("Before:\n",df)
    
if __name__ == "__main__":
    main()