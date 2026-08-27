import schedule
import time
import datetime
import os

def ScanFile(File):

    try:
        if not os.path.isfile(File):
            print("Error: Files does not exists:")
            return
    
        with open(File, "r") as fobj:
            Data = fobj.read()

            if len(Data) == 0:
                print("File is empty")
            else:
                print("_______________")
                print("Content of the file :")
                print("________________")
                print(Data)

    except PermissionError:
        print("Error :Permissition denined")

    except OSError:
        print("Error : File Cannot be Opened")

def main():
    print("Automation Script Started...")

    File = input("Enter the file path: ")

   
    schedule.every(60).seconds.do(ScanFile, File)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()