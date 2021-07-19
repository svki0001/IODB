import pandas as pd
import random
from random import randrange
from lorem_text import lorem
from dbQuerys import dbQuerys

main_dir = ""
main_dir = "IODB/"

df = pd.read_csv(f"{main_dir}csvs/users.csv")

card_ids = df["cardID"]

for card_id in card_ids:
    if random.random() < 0.2:
        words = randrange(1, 15)
        note = lorem.words(words)
        dbQuerys.updateUserNote(note, card_id)
    