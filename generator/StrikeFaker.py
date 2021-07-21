from lorem_text import lorem
from random import randrange
import pandas as pd

class StrikeFaker:
    main_dir = ""
    #main_dir = "IODB/"

    def generateStrikes(self):
        n_strikes = int(100000 * 0.10)
        df = pd.read_csv(f"{self.main_dir}csvs/log_users.csv")
        sessIDs = df["sessionID"]
        sessionIDs = [sessIDs[randrange(0, n_strikes)] for n in range(n_strikes)]

        with open(f"{self.main_dir}csvs/strikes.csv", "w", encoding="utf-8") as dest:
            dest.write(f"sessionID,description")
            for sessionID in sessionIDs:
                count = randrange(3, 15)
                desc = lorem.words(count)
                dest.write(f"\n{sessionID},{desc}")