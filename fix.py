import random
from random import randrange
from lorem_text import lorem
import pandas as pd
from database.dbQuerys import update_user_note, select_contract_begin, update_contract_end

main_dir = "IODB/"

# users = pd.read_csv(f"{main_dir}csvs/users.csv")
# cardIDs = users["cardID"]

# for cardID in cardIDs:
#     if random.random() < 0.2:
#         words = randrange(1, 15)
#         note = lorem.words(words)
#         print(f"updating {cardID} note: {note}")
#         update_user_note(note, cardID)

contracts = pd.read_csv(f"{main_dir}csvs/contracts.csv")
contractIDs = contracts["contractID"]

for contractID in contractIDs:
    contractBegin = str(select_contract_begin(contractID))
    beginMonth = int(contractBegin.split("-")[1])
    if beginMonth >= 3 and beginMonth < 9:
        endMonth = 9
    else:
        endMonth = 3
    contractEnd= f"2021-{endMonth:02d}-01"
    print(f"updating {contractID} note: {contractEnd}")
    update_contract_end(contractID, contractEnd)