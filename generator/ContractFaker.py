import datetime
from random import randrange
import random
import pandas as pd
from unidecode import unidecode
import re
import loading_bar
import time

def generate_contracts():
    main_dir = ""
    
    # to detect duplicates
    contractIDs = set()

    # init time
    start_time = time.time()

    # read generated users data
    df = pd.read_csv(f"{main_dir}csvs/users.csv")

    emails = df["email"]
    prenames = df["prename"]
    surnames = df["surname"]
    usernames = df["username"]

    print("starting contracts generator...")
    with open(f"{main_dir}csvs/contracts.csv", "w", encoding="utf-8") as dest:
        dest.write(f"contractID,email,contractBegin,contractEnd,contractPath,contractPaid")
    
        length = len(emails)
        for i in range(length):
            
            tech = ["Ausstehend", "Gremien Mitg.", "Bezahlt"]
            weight = [1.5, 0.2, 3]
            contractPaidRandom= random.choices(tech, k = 1, weights = weight)

            email = emails[i]
            contractBegin_calc =datetime.datetime.today()-datetime.timedelta(days=randrange(0,30))
            contractBegin = contractBegin_calc.strftime("%Y-%m-%d")
            beforeBegin_calc= contractBegin_calc-datetime.timedelta(days=randrange(0,8))
            
            if re.search(r"0000", email):
                contractID = "AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(usernames[i])
            else:
                n = str(int(re.search(r"\d+", email).group()))
                contractID = "AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(usernames[i]) + n
            
            beginMonth = int(contractBegin.split("-")[1])
            if beginMonth >= 3 and beginMonth < 9:
                endMonth = 9
            else:
                endMonth = 3
            contractEnd= f"2021-{endMonth:02d}-01"
            
            contractPath="AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(prenames[i]) + "_" + str(surnames[i]) + ".pdf"
            contractPaid= contractPaidRandom[0]

            dest.write(f"\n{contractID},{email},{contractBegin},{contractEnd},{contractPath},{contractPaid}")
            loading_bar.print_loading_bar(current=i, max=length)

    end_time = time.time()
    print()
    print(f"finished in {int((end_time - start_time) / 60)} minutes!")