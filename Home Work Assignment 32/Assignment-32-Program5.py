
import os
import schedule
import time
import datetime

# Function to delete empty files
def DeleteEmptyFiles(Directory):

    LogFile = "DeleteLog.txt"

    with open(LogFile, "a") as log:

        log.write("\n=====================================\n")
        log.write("Delete Operation : " + str(datetime.datetime.now()) + "\n")
        log.write("=====================================\n")

        # Scan directory recursively
        for FolderName, SubFolderNames, FileNames in os.walk(Directory):

            for File in FileNames:

                FilePath = os.path.join(FolderName, File)

                try:
                    # Check file size
                    if os.path.getsize(FilePath) == 0:

                        os.remove(FilePath)

                        print("Deleted :", FilePath)

                        log.write("Deleted : " + FilePath + "\n")

                except PermissionError:

                    print("Permission denied :", FilePath)

                    log.write("Permission denied : " + FilePath + "\n")

                except Exception as e:

                    print("Error :", FilePath)

                    log.write("Error : " + FilePath + " -> " + str(e) + "\n")

        log.write("=====================================\n")


def main():

    print("Automation Script Started...")

    Directory = input("Enter directory path : ")

    # Validate directory
    if not os.path.isdir(Directory):
        print("Directory does not exist.")
        return

    print("Directory exists.")
    print("Scanning every 1 hour...\n")

    # Run once immediately
    DeleteEmptyFiles(Directory)

    # Schedule every hour
    schedule.every(1).hours.do(DeleteEmptyFiles, Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



