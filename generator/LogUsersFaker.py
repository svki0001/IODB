from faker import Faker
import pandas as pd
from random import randrange
from datetime import timedelta
import random
import time
import loading_bar

def generate_log_users():
    n_log_users = 100000
    main_dir = ""

    # init faker
    faker = Faker()

    # init time
    start_time = 0

    # get generated cardIDs
    users = pd.read_csv(f"{main_dir}csvs/users.csv")
    u_cardIDs = users["cardID"]

    # init time
    start_time = time.time()

    print("starting log users generator...")
    with open(f"{main_dir}csvs/log_users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,checkIn,checkOut")
        

        for i in range(n_log_users):
            cardID = random.choice(u_cardIDs)
            checkIn = faker.date_time_between(start_date="-1y", end_date="-1d")
            
            sessionTimeMinutes = randrange(180) + 1
            checkOut = checkIn + timedelta(minutes=sessionTimeMinutes)
            
            checkInStr = checkIn.strftime("%Y-%m-%d %H:%M:%S")
            checkOutStr = checkOut.strftime("%Y-%m-%d %H:%M:%S")
            
            dest.write(f"\n{cardID},{checkInStr},{checkOutStr}")
            loading_bar.print_loading_bar(current=i, max=n_log_users)

    end_time = time.time()
    print()
    print(f"finished in {int((end_time - start_time) / 60)} minutes!")



# class LogUsersFaker:
#     faker = None

#     def __init__(self) -> None:
#         self.faker = Faker()

#     def get_cardID(self):
#         return dbQuerys.get_random_cardID()

#     def get_checkIn(self):
#         return self.faker.date_time_between(start_date="-1y", end_date="-1d")

#     def get_checkOut(self, check_in):
#         sessionTimeMinutes = randrange(180) + 1
#         return check_in + timedelta(minutes=sessionTimeMinutes)