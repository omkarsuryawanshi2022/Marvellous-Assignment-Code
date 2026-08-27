import pandas as pd

def OneHotenCoding():
    data = {
        'Userid' : [101,121,151,151],
        'Gendar':  ['male','female','male','female']

    }

    df = pd.DataFrame(data)

    print("Original data is there:\n",data)

    # perform one hot encoding

    df_encoded = pd.get_dummies(df,columns=['Gendar'],dtype=int)

    print("converted original data to hot encoding data: \n",df_encoded)



def main():
    
    OneHotenCoding()

if __name__ == "__main__":
    main()