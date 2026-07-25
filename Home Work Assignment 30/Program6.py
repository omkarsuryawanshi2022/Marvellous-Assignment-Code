import sys
import schedule
import time
import datetime

def LunchTime():

    print("LunchTime is :",datetime.datetime.now())

def WrapupWork():

    print("Wrap up Work every day at  :",datetime.datetime.now())


def main():
    print("Automation Script Started")

    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("18:00").do(WrapupWork)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ =="__main__":
    main()