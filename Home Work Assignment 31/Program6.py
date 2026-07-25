import schedule
import time

def Monday():
        print("Start your Weekly goals:")

def Wednesday():
            print("Review your Weekly progress:")

def Friday():
            print("Weekly Work Completed:")

    
def main():
    print("Automation Script Started...")

    schedule.every().monday.at("13:00").do(Monday)

    schedule.every().wednesday.at("17:00").do(Wednesday)

    schedule.every().friday.at("18:00").do(Friday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()