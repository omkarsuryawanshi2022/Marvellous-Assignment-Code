import schedule
import time
import datetime

def CreateLogFile():
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create log file name
    filename = f"Marvellous_Log{timestamp}.txt"

    # Create and write into the file
    with open(filename, "w") as fobj:
        fobj.write("=====================================\n")
        fobj.write("      Marvellous Automation Log\n")
        fobj.write("=====================================\n")
        fobj.write(f"Log File Created At : {datetime.datetime.now()}\n")

    print(f"New Log File Created : {filename}")

def main():
    print("Automation Script Started...")

    # Schedule every 10 minutes
    schedule.every(1).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()