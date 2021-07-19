import dbquery
import time
import csv
import datetime
from random import randrange

#main_dir = "IODB/"
main_dir = "C:/Users/klein/OneDrive/Desktop/abgabe/src/app/csvs/contract2.csv"

users_dir = "C:/Users/klein/OneDrive/Desktop/abgabe/src/app/csvs/users2.csv"

EmailFromUser = []
PrenameFromUser = []
SurnameFromUser = []
UsernameFromUser = []


def write():
            with open(f"{main_dir}", "w", encoding="utf-8") as dest:
                dest.write(f"contractID,email,contractBegin,contractEnd,contractPath,contractPaid")
                print("starting generator...")
           
                length = len(EmailFromUser)
                for i in range(length):


                    email = EmailFromUser[i]
                    contractBegin_calculate =datetime.datetime.today()-datetime.timedelta(days=randrange(0,30))
                    contractBegin = (contractBegin_calculate).strftime('%Y-%m-%d')
                    bevoreBegin_calculate= contractBegin_calculate-datetime.timedelta(days=randrange(0,8))
                    bevoreBegin=(contractBegin_calculate-datetime.timedelta(days=randrange(0,8))).strftime('%Y-%m-%d')
                    contractID = "AZW-"+str((bevoreBegin_calculate).strftime('%Y-%m-%d'))+"_"+str(UsernameFromUser[i])
                    contractEnd="2021-"+str(randrange(1,7))+"01"
                    contractPath="AZW-"+str((bevoreBegin_calculate).strftime('%Y-%m-%d'))+"_"+str(PrenameFromUser[i])+"_"+str(SurnameFromUser[i])+".pdf"
                    contractPaid="Ausstehend"
                    dest.write(f"{contractID},{email},{contractBegin},{contractEnd},{contractPath},{contractPaid}\n")
            

if __name__ == "__main__":

    with open(f"{users_dir}", encoding="utf-8", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            print("drin")
            EmailFromUser.append(str(row['email']))
            PrenameFromUser.append(str(row['prename']))
            SurnameFromUser.append(str(row['surname']))
            UsernameFromUser.append( str(row['username']))
            
        write()


