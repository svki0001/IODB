import pandas as pd
import random
from random import randrange
from lorem_text import lorem
from database.dbQuerys import dbQuerys

class UserNotesFaker:
    main_dir = ""
    main_dir = ""

    users_path = f"{main_dir}csvs/users.csv"

    def generateUserNotes(self):
        df = pd.read_csv(self.users_path)
        card_ids = df["cardID"]

        for card_id in card_ids:
            if random.random() < 0.2:
                words = randrange(1, 15)
                note = lorem.words(words)
                df.loc[df.cardID == card_id, "cardID"] = note
                dbQuerys.updateUserNote(note, card_id)

        df.to_csv(self.users_path, ",", line_terminator="\n", index=False, header=False)
    