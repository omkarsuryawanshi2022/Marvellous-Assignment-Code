# count Line in a File

import sys

def main():
    print("Enter file name:")
    FileName = input()

    try:
        with open("Demo.txt", "r") as fp:


            Lines = sum(1 for line in fp)



            print("File present line count is :",Lines)

        
            fp.close()

 
    except FileNotFoundError:
        print("Source file doed not exist")
    
if __name__ == "__main__":
    main()