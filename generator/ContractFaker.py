import datetime
from random import randrange
import random
import pandas as pd
from unidecode import unidecode
import re

contractIDs = set()

class ContractFaker:
    main_dir = ""
    # main_dir = "IODB/"

    df = pd.read_csv(f"{main_dir}csvs/users.csv")

    emails = df["email"]
    prenames = df["prename"]
    surnames = df["surname"]
    usernames = df["username"]

    # print(emails)

    def generateContracts(self):
        with open(f"{self.main_dir}csvs/contracts.csv", "w", encoding="utf-8") as dest:
            dest.write(f"contractID,email,contractBegin,contractEnd,contractPath,contractPaid")
            print("starting generator...")
        
            length = len(self.emails)
            for i in range(length):
                
                tech = ["Ausstehend", "Gremien Mitg.", "Bezahlt"]
                weight = [1.5, 0.2, 3]
                contractPaidRandom= random.choices(tech, k = 1, weights = weight)

                email = self.emails[i]
                contractBegin_calc =datetime.datetime.today()-datetime.timedelta(days=randrange(0,30))
                contractBegin = contractBegin_calc.strftime("%Y-%m-%d")
                beforeBegin_calc= contractBegin_calc-datetime.timedelta(days=randrange(0,8))
                
                if re.search(r"0000", email):
                    contractID = "AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(self.usernames[i])
                else:
                    n = str(int(re.search(r"\d+", email).group()))
                    contractID = "AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(self.usernames[i]) + n
                    
                contractEnd="2021-" + str(randrange(1,7)) + "01"
                contractPath="AZW-" + str(beforeBegin_calc.strftime("%Y-%m-%d")) + "_" + str(self.prenames[i]) + "_" + str(self.surnames[i]) + ".pdf"
                contractPaid= contractPaidRandom[0]
                dest.write(f"\n{contractID},{email},{contractBegin},{contractEnd},{contractPath},{contractPaid}")
