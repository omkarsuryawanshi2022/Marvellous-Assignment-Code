# copy file content into new file mean command line argument

import sys
import filecmp

def main():
    if len(sys.argv)!=3:
        print("python 4.py <FileName>")
        return
    SourceFile = sys.argv[2]

    try:
        fSource = open(SourceFile,"r")

        Data = fSource.read()

        are_identical = filecmp.cmp('ABC.txt', 'Demo.txt', shallow=False)

        if are_identical:
            print("The files are Same content.")
        else:
            print("The files have different contents.")
  
        fSource.close()

       
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()