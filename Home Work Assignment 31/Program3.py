import schedule
import time
import datetime
import os

def ScanDirectory(Directory):
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create log file name
    filename = f"Scan_SpecifiedDirectory{timestamp}.txt"

    # count only file
    fileCount = 0
    FoldarCount = 0

    for Foldarname , SubFoldarname, Filesnames in os.walk(Directory):
        fileCount += len(Filesnames)
        FoldarCount += len(SubFoldarname)

    # Create and write into the file
    with open(filename, "w") as fobj:
        fobj.write("=====================================\n")
        fobj.write("      Marvellous Automation Log\n")
        fobj.write("=====================================\n")
        fobj.write(f"SubFoldar  is :,{FoldarCount}\n")
        fobj.write(f"number of files are :,{fileCount}\n")
        fobj.write(f"Directory Scanned are :,{Directory}\n")
        fobj.write(f"Log File Created Date and Time : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")

    print(f"New Log File Created : {filename}")

def main():
    print("Automation Script Started...")

    Directory = input("Enter the directory path:")

    if os.path.isdir(Directory):
        print("Directory path exists:")
    else:
        print("Directory path does not exists:")
        return

    # Schedule every 1 minutes
    schedule.every(1).minutes.do(ScanDirectory,Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()