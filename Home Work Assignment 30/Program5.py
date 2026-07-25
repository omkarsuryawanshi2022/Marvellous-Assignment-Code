import schedule
import time
import datetime

def Display():

    fobj = open("Marvellous.txt", "a")

    Ret = datetime.datetime.now()

    fobj.write(str(Ret) + "\n")

    fobj.close()


def main():
    print("Automation Script Started")

    schedule.every(10).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()