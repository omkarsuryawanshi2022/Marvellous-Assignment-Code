import schedule
import time
import datetime

def Display(Message):
    print(Message,datetime.datetime.now())


def main():

    print("Automation Script Started")

    UserMessage = input("Enter the message :")

    Interval = int(input("enter the time interval in second :"))

    # validation
    if Interval < 0:
        print("Error : time interval must be gretter than 0.")
        return

    schedule.every(Interval).seconds.do(Display,UserMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End Of Automation Script:")



if __name__ == "__main__":
    main()