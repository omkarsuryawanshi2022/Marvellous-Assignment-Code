# Search a word in a File

import sys

def main():
    print("Enter file name:")
    FileName = input()

    print("Enter the word search:")
    SearchWord  = input()


    try:
        fobj = open(FileName,"r")

        Data = fobj.read()

        if SearchWord in  Data:
            print(SearchWord,"is present in the file")
        else:
            print(SearchWord,"is not present in the file")
        
        fobj.close()

 
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()