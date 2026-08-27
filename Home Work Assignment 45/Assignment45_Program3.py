import pandas as pd

def average_marks ():
    data = {
        'Marks' : [101,121,151,171],
        'Gendar':  ['male','female','male','female'],
        'Name': ['omkar','sanket','amit','prasad']

    }

    df = pd.DataFrame(data)

    AVmarks = df.groupby('Gendar')['Marks'].mean()

    print("Average marks is :",AVmarks)

    



def main():
    
    average_marks ()

if __name__ == "__main__":
    main()