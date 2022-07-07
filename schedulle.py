import csv
import time

# Schedule Library imported
import schedule

from bot_telegram import tele


# Functions setup
def sudo_placement():
  print("Get ready for Sudo Placement at Geeksforgeeks")

def good_luck():
  print("Good Luck for Test")

def work():
  print("Study and work hard")

def bedtime():
  print("It is bed time go rest")
  
def geeks():
    with open('registry.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        for row in csv_reader:
            print(row)
            tele(row[0], row[1])
# Task scheduling
# After every 10mins geeks() is called.
schedule.every(300).seconds.do(geeks)

# After every hour geeks() is called.
# schedule.every().hour.do(geeks)

# # Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("23:12").do(bedtime)

# # After every 5 to 10mins in between run work()
# schedule.every(5).to(10).minutes.do(work)

# # Every monday good_luck() is called
# schedule.every().monday.do(good_luck)

# # Every tuesday at 18:00 sudo_placement() is called
# schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
def start_schedule():
    while True:
    # Checks whether a scheduled task
    # is pending to run or not
        schedule.run_pending()
        time.sleep(60)
        print(".......")


