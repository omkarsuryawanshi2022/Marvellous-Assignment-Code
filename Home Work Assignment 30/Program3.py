import schedule
import time
import datetime

def DisplayCurrentDatetime():

    print("Coding Kar...!")


def main():
    print("Automation Script Started")

    schedule.every(30).minutes.do(DisplayCurrentDatetime)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End Of Automation Script:")



if __name__ == "__main__":
    main()