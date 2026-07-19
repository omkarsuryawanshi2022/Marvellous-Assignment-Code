# Check whether file exists in current directory

import os

def main():
    print("Enter file name:")
    FileName = input()

    if os.path.exists(FileName):
        print(FileName, "exists in the current directory.")
    else:
        print(FileName, "does not exist in the current directory.")

if __name__ == "__main__":
    main()