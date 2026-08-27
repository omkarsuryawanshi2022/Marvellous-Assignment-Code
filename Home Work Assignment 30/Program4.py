import schedule
import time
import datetime

def Display():

    print("Coding Kar...!")


def main():
    print("Automation Script Started")

    schedule.every().days.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End Of Automation Script:")


if __name__ == "__main__":
    main()