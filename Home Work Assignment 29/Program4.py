# Copy file content into anather file

import sys

def main():
    print("Enter First file name:")
    FileName1 = input()

    print("Enter Second file name:")
    FileName2 = input()

    try:
        fSource = open(FileName1,"r")

        fDistination = open(FileName2,"w")

        Data = fSource.read()

        Data = fDistination.write(Data)

        print("Content copied sucessfully")

        fSource.close()

        fDistination.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    
if __name__ == "__main__":
    main()