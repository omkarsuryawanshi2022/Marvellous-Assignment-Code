# Feequency of a string in file

import sys

def main():
    print("Enter file name:")
    FileName = input()

    SearchString = input("Enter the String:")


    try:
        fSource = open(FileName,"r")

        Data = fSource.read()

        Count = Data.count(SearchString)

        print("Frequency of ",SearchString, "is",Count)

        fSource.close()
 
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()