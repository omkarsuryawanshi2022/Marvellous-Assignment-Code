import schedule
import time
import datetime

def DisplayMessage(Message):
    print(Message)

def main():

    print("Automation Script Started")

    UserMessage = input("Enter the message :")

    schedule.every(5).seconds.do(DisplayMessage,UserMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End Of Automation Script:")



if __name__ == "__main__":
    main()