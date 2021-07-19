import pandas as pd
from dbQuerys import dbQuerys

# main_dir = "IODB/"
main_dir = ""

df = pd.read_csv(f"{main_dir}csvs/users.csv", sep=",")

def import_users():
    with open(f"{main_dir}csvs/users.csv", "r") as src:
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

def update_user():

def import_strikes():
    with open(f"{main_dir}csvs/strikes.csv", "r") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addStrike(
                    line[0],
                    line[1],
                    line[2]
                )
                print(f"imported strike with strikeID {line[0]}")
            i += 1
            
def import_log_users():
    with open(f"{main_dir}csvs/log_users.csv", "r") as src:
        i = 0
        for line in src.read().split("\n"):
            if i:
                line = line.split(",")
                dbQuerys.addLog(
                    line[0],
                    line[1],
                    line[2],
                    line[3]
                )
                print(f"imported log with sessionID {line[0]}")
            i += 1
            
def import_contracts():
    with open(f"{main_dir}csvs/contracts.csv", "r") as src:
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
                print(f"imported contract with contractID {line[0]}")
            i += 1

#import_users()
import_log_users()