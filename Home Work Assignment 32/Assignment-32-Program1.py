import schedule
import time
import datetime
import os

def Createnewtextfileeverymin():
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create log file name
    filename = f"Files_{timestamp}.txt"

    # Create and write into the file
    with open(filename, "w") as fobj:
        
       
        fobj.write(f"Files_ :,{filename}\n")
        fobj.write(f"Log File Created Date and Time : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")

    print(f"New Log File Created : {filename}")

def main():
    print("Automation Script Started...")

    # Schedule every 1 minutes
    schedule.every(1).minutes.do(Createnewtextfileeverymin)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()