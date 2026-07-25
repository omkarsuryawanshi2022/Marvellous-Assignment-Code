import os
import shutil
import schedule
import time
import datetime

# Function to copy .txt files
def CopyTextFiles(SourceDir, DestDir):

    # Log file name
    LogFile = "CopyLog.txt"

    with open(LogFile, "a") as log:

        log.write("\n====================================\n")
        log.write("Copy Operation : " + str(datetime.datetime.now()) + "\n")
        log.write("====================================\n")

        # Scan source directory
        for File in os.listdir(SourceDir):

            SourcePath = os.path.join(SourceDir, File)

            # Copy only .txt files
            if os.path.isfile(SourcePath) and File.endswith(".txt"):

                DestinationPath = os.path.join(DestDir, File)

                try:
                    shutil.copy2(SourcePath, DestinationPath)

                    print(File, "copied successfully.")

                    log.write(File + " -> Copied Successfully\n")

                except Exception as e:

                    print("Failed to copy :", File)

                    log.write(File + " -> Failed : " + str(e) + "\n")

        log.write("====================================\n")


def main():

    print("Automation Script Started...")

    SourceDir = input("Enter Source Directory : ")
    DestDir = input("Enter Destination Directory : ")

    # Validate Source Directory
    if not os.path.isdir(SourceDir):
        print("Source directory does not exist.")
        return

    # Validate Destination Directory
    if not os.path.isdir(DestDir):
        print("Destination directory does not exist.")
        return

    print("Both directories are valid.")
    print("Copy process will run every 10 minutes...\n")

    # Schedule every 10 minutes
    schedule.every(10).minutes.do(CopyTextFiles, SourceDir, DestDir)

    # Run once immediately (optional)
    CopyTextFiles(SourceDir, DestDir)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

