# count word in a file 

import sys

def main():
    print("Enter file name:")
    FileName = input()

    try:
        with open(FileName, "r") as f:

            Data = f.read()

            Words = Data.split()

            Count = len(Words)

            print("in that file total word count is ",Count)
            f.close()

 
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()