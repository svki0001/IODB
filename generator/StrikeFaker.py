from lorem_text import lorem
from random import randrange
import pandas as pd
import time
import loading_bar

def generate_strikes():
    n_strikes = int(100000 * 0.10)
    main_dir = ""

    # init time
    start_time = 0

    # get sessionIDs from generated user logs
    df = pd.read_csv(f"{main_dir}csvs/log_users.csv")

    sessIDs = df["sessionID"]
    sessionIDs = [sessIDs[randrange(0, n_strikes)] for n in range(n_strikes)]

    # init time
    start_time = time.time()

    print("starting strikes generator...")
    with open(f"{main_dir}csvs/strikes.csv", "w", encoding="utf-8") as dest:
        dest.write(f"sessionID,description")

        for sessionID in sessionIDs:
            count = randrange(3, 15)
            desc = lorem.words(count)
            dest.write(f"\n{sessionID},{desc}")
            loading_bar.print_loading_bar(current=i, max=n_strikes)

    end_time = time.time()
    print()
    print(f"finished in {int((end_time - start_time) / 60)} minutes!")