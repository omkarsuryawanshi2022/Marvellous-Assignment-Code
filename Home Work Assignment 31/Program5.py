import schedule
import time
import datetime
import os

def CreateLogFile(Directory):
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create log file name
    filename = f"DirectoryCountLog{timestamp}.txt"

    # count only file
    fileCount = 0
    for Foldarname , SubFoldarname, Filesnames in os.walk(Directory):
        fileCount += len(Filesnames)

    # Create and write into the file
    with open(filename, "w") as fobj:
        fobj.write("=====================================\n")
        fobj.write("      Marvellous Automation Log\n")
        fobj.write("=====================================\n")
        fobj.write(f"Directory path is :,{Directory}\n")
        fobj.write(f"number of files are :,{fileCount}\n")
        fobj.write(f"Log File Created Date and Time : {datetime.datetime.now()}\n")

    print(f"New Log File Created : {filename}")

def main():
    print("Automation Script Started...")

    Directory = input("Enter the directory path:")

    # Schedule every 10 minutes
    schedule.every(1).minutes.do(CreateLogFile,Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()