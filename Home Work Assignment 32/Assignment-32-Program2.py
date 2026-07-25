import schedule
import time
import datetime
import os


def ScanFile(File):
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create log file name
    filename = f"Log{timestamp}.txt"

    # Get size of the specified file
    file_size = os.path.getsize(File)

    # Create and write into the log file
    with open(filename, "a") as fobj:
        fobj.write("=====================================\n")
        fobj.write("      Marvellous Automation Log\n")
        fobj.write("=====================================\n")
        fobj.write(f"File Path : {File}\n")
        fobj.write(f"File Size : {file_size} Bytes\n")
        fobj.write(f"Date and Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
        fobj.write("=====================================\n")

    print(f"New Log File Created : {filename}")


def main():
    print("Automation Script Started...")

    File = input("Enter the file path: ")

    if os.path.isfile(File):
        print("File path exists.")
    else:
        print("File path does not exist.")
        return

    # Schedule every 30 seconds
    schedule.every(30).seconds.do(ScanFile, File)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()