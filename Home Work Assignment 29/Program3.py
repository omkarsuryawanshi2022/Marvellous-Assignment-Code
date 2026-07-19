# count word in a file 

import sys

def main():
    print("Enter file name:")
    FileName = input()

    try:
        with open(FileName, "r") as f:

            Data = f.read()

            print(Data)

           
            f.close()

 
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()