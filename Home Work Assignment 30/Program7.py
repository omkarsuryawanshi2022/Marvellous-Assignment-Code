import os
import shutil
import datetime

def main():

    # Accept Source File Path
    sourcefile = input("Enter the source file path : ")

    # Accept Destination Folder Path
    DestinationFolder = input("Enter the destination folder path : ")

    # Check Source File
    if not os.path.exists(sourcefile):
        print("Source file does not exist.")
        return

    print("Source file exists.")

    # Check Destination Folder
    if not os.path.exists(DestinationFolder):
        print("Destination folder does not exist.")
        return

    print("Destination folder exists.")

    # Extract File Name and Extension
    filename = os.path.basename(sourcefile)

    name, extension = os.path.splitext(filename)

    print("File Name      :", name)
    print("Extension      :", extension)

    # Get Current Date & Time
    CurrentDateTime = datetime.datetime.now()

    # Create Timestamp
    TimeStamp = CurrentDateTime.strftime("%d_%m_%Y_%H_%M_%S")

    # Create Backup File Name
    BackupFileName = f"{name}_{TimeStamp}{extension}"

    print("Backup File Name :", BackupFileName)

    # Create Destination Path
    DestinationPath = os.path.join(DestinationFolder, BackupFileName)

    print("Destination Path :", DestinationPath)

    # Copy File
    shutil.copy2(sourcefile, DestinationPath)

    # Create/Open Log File
    LogFile = open("backup_log.txt", "a")

    # Log Time
    LogTime = CurrentDateTime.strftime("%d-%m-%Y %I:%M:%S %p")

    # Write Log Entry
    LogFile.write(f"Backup completed successfully at {LogTime}\n")

    # Close Log File
    LogFile.close()

    # Success Message
    print("Backup completed successfully.")
    print("Backup file created :", BackupFileName)


if __name__ == "__main__":
    main()