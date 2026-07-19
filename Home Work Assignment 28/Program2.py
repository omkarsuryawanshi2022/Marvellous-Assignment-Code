# Display the Content

import os

def main():
    print("Enter file name:")
    FileName = input()

    try:
        fobj = open(FileName,"r")
        print("File gets opened")

        Data = fobj.read()
        print(Data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in Current directory")

        


if __name__ == "__main__":
    main()