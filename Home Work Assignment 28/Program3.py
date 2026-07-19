# copy file content into new file mean command line argument

import sys


def main():
    if len(sys.argv)!=2:
        print("python 3.py <FileName>")
        return
    SourceFile = sys.argv[1]

    try:
        fSource = open(SourceFile,"r")

        fDistination = open("Demo.txt","w")

        Data = fSource.read()

        fDistination.write(Data)

        print("Content copied sucessfully in Demo.txt")

        fSource.close()

        fDistination.close()

    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()