import pandas as pd
from database.dbQuerys import dbQuerys

main_dir = ""
main_dir = "IODB/"

df = pd.read_csv(f"{main_dir}csvs/users.csv", sep=",")

def import_users():
    print("starting import of users.csv")
    with open(f"{main_dir}csvs/users.csv", "r", encoding="utf-8") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addUser(
                    line[0],
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                    line[5],
                    line[6],
                    line[7],
                    line[8],
                    line[9],
                    line[10],
                    line[11],
                    line[12],
                    line[13]
                )
                print(f"imported {line[0]}")
            i += 1

def import_strikes():
    print("starting import of strikes.csv")
    with open(f"{main_dir}csvs/strikes.csv", "r", encoding="utf-8") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addStrike(
                    line[0],
                    line[1]
                )
                print(f"imported {line[0]}")
            i += 1
            
def import_log_users():
    print("starting import of log_users.csv")
    with open(f"{main_dir}csvs/log_users.csv", "r", encoding="utf-8") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addLog(
                    line[0],
                    line[1],
                    line[2]
                )
                print(f"imported {line[0]}")
            i += 1
            
def import_contracts():
    print("starting import of contracts.csv")
    with open(f"{main_dir}csvs/contracts.csv", "r", encoding="utf-8") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addContract(
                    line[0],
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                    line[5]
                )
                print(f"imported {line[0]}")
            i += 1

#import_users()
# import_log_users()